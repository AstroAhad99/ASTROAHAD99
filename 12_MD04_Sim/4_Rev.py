import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation

# Define conveyor and box parameters
conveyor_width = 200  # Width of conveyor in pixels
conveyor_height = 600  # Height of conveyor in pixels
box_size = 30  # Size of each box in pixels
gap = 20  # Required gap between tail of one box and head of the next box in pixels
exit_position = 550  # Position where boxes exit the conveyor
lanes_y = [0, 150, 300, 450]  # Y-positions for each lane

# Box class representing each parcel
class Box:
    def __init__(self, ax, lane_y, box_id, initial_x):
        self.lane_y = lane_y
        self.box_id = box_id
        self.x_pos = initial_x
        self.speed = 2  # Initial speed
        self.rect = patches.Rectangle((self.x_pos, lane_y), box_size, box_size, linewidth=1, edgecolor='black', facecolor='white')
        self.text = ax.text(self.x_pos + box_size / 4, lane_y + box_size / 4, str(self.box_id), ha='center', va='center', fontsize=8, color='black')
        ax.add_patch(self.rect)

    def move(self):
        self.x_pos += self.speed
        self.rect.set_x(self.x_pos)
        self.text.set_x(self.x_pos + box_size / 4)

    def remove(self):
        self.rect.remove()
        self.text.remove()

# Conveyor class to manage boxes on a single lane
class Conveyor:
    def __init__(self, ax, lane_y, conveyor_id, interface):
        self.ax = ax
        self.lane_y = lane_y
        self.conveyor_id = conveyor_id
        self.interface = interface  # Interface to interact with other conveyors
        self.boxes = []
        self.initialize_boxes()

    def initialize_boxes(self):
        # Initialize a set of boxes with slight x-offsets for this conveyor
        offsets = [0, 5, 10, 15]
        self.boxes = [Box(self.ax, self.lane_y, idx + 1, offsets[idx]) for idx in range(len(offsets))]

    def update_positions(self):
        # Update the position of each box and manage spacing
        for box in self.boxes:
            if box.x_pos < exit_position:
                # Get the next box on the same conveyor
                next_box = self.get_next_box(box)

                # Determine speed based on the gap requirement
                if next_box:
                    distance_to_next_box = next_box.x_pos - (box.x_pos + box_size)
                    if distance_to_next_box < gap:
                        box.speed = 1  # Slow down if the distance is less than the gap
                    elif distance_to_next_box > gap:
                        box.speed = 2  # Speed up if distance is greater than gap

                # Check for boxes on adjacent conveyors to maintain inter-lane gap
                adjacent_boxes = self.interface.get_adjacent_boxes(self.conveyor_id, box)
                for adj_box in adjacent_boxes:
                    distance_to_adj_box = adj_box.x_pos - (box.x_pos + box_size)
                    if distance_to_adj_box < gap:
                        box.speed = 1
                    elif distance_to_adj_box > gap and box.speed < 2:
                        box.speed = 2

                box.move()
            else:
                # Remove box if it reaches the exit
                box.remove()
                self.boxes.remove(box)

        # Reinitialize boxes if all have exited
        if not self.boxes:
            self.initialize_boxes()

    def get_next_box(self, current_box):
        # Find the next box in the same lane that is ahead of the current box
        same_lane_boxes = [box for box in self.boxes if box.x_pos > current_box.x_pos]
        if same_lane_boxes:
            return min(same_lane_boxes, key=lambda b: b.x_pos)
        return None

# Conveyor interface to manage interactions between conveyors
class ConveyorInterface:
    def __init__(self):
        self.conveyors = {}

    def register_conveyor(self, conveyor):
        self.conveyors[conveyor.conveyor_id] = conveyor

    def get_adjacent_boxes(self, conveyor_id, box):
        # Return boxes in the adjacent lanes that are near the current box
        adjacent_boxes = []
        if conveyor_id - 1 in self.conveyors:
            adjacent_boxes.extend([b for b in self.conveyors[conveyor_id - 1].boxes if b.x_pos > box.x_pos])
        if conveyor_id + 1 in self.conveyors:
            adjacent_boxes.extend([b for b in self.conveyors[conveyor_id + 1].boxes if b.x_pos > box.x_pos])
        return adjacent_boxes

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(0, conveyor_width)
ax.set_ylim(-50, conveyor_height + 50)
ax.axis('off')

# Draw conveyor lane borders
for lane_y in lanes_y:
    ax.plot([0, conveyor_width], [lane_y, lane_y], color='gray', linestyle='-', linewidth=2)

# Create ConveyorInterface and Conveyor objects
interface = ConveyorInterface()
conveyors = []
for idx, lane_y in enumerate(lanes_y):
    conveyor = Conveyor(ax, lane_y, idx, interface)
    conveyors.append(conveyor)
    interface.register_conveyor(conveyor)

# Update function for animation
def update(frame):
    for conveyor in conveyors:
        conveyor.update_positions()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
