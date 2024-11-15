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
    def __init__(self, ax, lane_y, box_id, initial_x, priority):
        self.lane_y = lane_y
        self.box_id = box_id
        self.priority = priority
        self.x_pos = initial_x
        self.speed = 2  # Initial speed
        self.rect = patches.Rectangle((self.x_pos, lane_y), box_size, box_size, linewidth=1, edgecolor='black', facecolor='white')
        self.text = ax.text(self.x_pos + box_size / 4, lane_y + box_size / 4, str(self.priority), ha='center', va='center', fontsize=8, color='black')
        ax.add_patch(self.rect)

    def move(self):
        self.x_pos += self.speed
        self.rect.set_x(self.x_pos)
        self.text.set_x(self.x_pos + box_size / 4)

    def remove(self):
        self.rect.remove()
        self.text.remove()

# Conveyor class to manage a single box on a single lane
class Conveyor:
    def __init__(self, ax, lane_y, conveyor_id, interface, priority):
        self.ax = ax
        self.lane_y = lane_y
        self.conveyor_id = conveyor_id
        self.interface = interface  # Interface to interact with other conveyors
        self.box = Box(self.ax, self.lane_y, conveyor_id + 1, 0, priority)  # Initialize one box with priority
        self.interface.register_box(self.box)  # Register box with interface

    def update_position(self):
        if self.box:
            if self.box.x_pos < exit_position:
                # Get the next box in terms of priority
                next_box = self.interface.get_next_priority_box(self.box.priority)

                # Determine speed based on gap requirement with the next lower-priority box
                if next_box:
                    distance_to_next_box = next_box.x_pos - (self.box.x_pos + box_size)
                    if distance_to_next_box < gap:
                        self.box.speed = 1  # Slow down if the distance is less than the gap
                    else:
                        self.box.speed = 2  # Speed up if distance is sufficient

                self.box.move()
            else:
                # Remove the box if it reaches the exit
                self.box.remove()
                self.interface.unregister_box(self.box)
                # Initialize a new box with the same priority after the previous box exits
                self.box = Box(self.ax, self.lane_y, self.conveyor_id + 1, 0, self.box.priority)
                self.interface.register_box(self.box)

# Conveyor interface to manage interactions between conveyors
class ConveyorInterface:
    def __init__(self):
        self.boxes = []

    def register_box(self, box):
        self.boxes.append(box)

    def unregister_box(self, box):
        if box in self.boxes:
            self.boxes.remove(box)

    def get_next_priority_box(self, current_priority):
        # Get the next lower-priority box
        lower_priority_boxes = [box for box in self.boxes if box.priority > current_priority]
        if lower_priority_boxes:
            # Return the box with the closest priority to the current box
            return min(lower_priority_boxes, key=lambda b: b.priority)
        return None

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
# Assign priorities 1, 2, 3, and 4 for each conveyor
priorities = [2, 1, 4, 3]  # Based on the example image you provided
for idx, lane_y in enumerate(lanes_y):
    conveyor = Conveyor(ax, lane_y, idx, interface, priorities[idx])
    conveyors.append(conveyor)

# Update function for animation
def update(frame):
    for conveyor in conveyors:
        conveyor.update_position()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
