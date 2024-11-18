import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation
import random

# Define conveyor and box parameters
conveyor_width = 200  # Width of conveyor in pixels
conveyor_height = 600  # Height of conveyor in pixels
box_size = 30  # Size of each box in pixels
gap = 40  # Required gap between tail of one box and head of the next box in pixels
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
    def __init__(self, ax, lane_y, conveyor_id, interface):
        self.ax = ax
        self.lane_y = lane_y
        self.conveyor_id = conveyor_id
        self.interface = interface  # Interface to interact with other conveyors
        self.box = None  # Initialize without a box
        self.initialize_box()  # Initialize the first box

    def initialize_box(self):
        # Create a new box with a random starting position and a placeholder priority
        initial_x = random.randint(0, 15)
        self.box = Box(self.ax, self.lane_y, self.conveyor_id + 1, initial_x, 0)  # Priority will be set later
        self.interface.register_box(self.box)

    def update_position(self):
        if self.box:
            if self.box.x_pos < exit_position:
                # Get the next lower-priority box
                next_box = self.interface.get_next_priority_box(self.box.priority)

                # Adjust speed based on the gap requirement with the next lower-priority box
                if next_box:
                    distance_to_next_box = next_box.x_pos - (self.box.x_pos + box_size)
                    if distance_to_next_box < gap:
                        self.box.speed = 1  # Slow down if the distance is less than the gap
                    else:
                        self.box.speed = 2  # Speed up if distance is sufficient

                # Move the box
                self.box.move()
            else:
                # Remove the box if it reaches the exit
                self.box.remove()
                self.interface.unregister_box(self.box)
                self.box = None  # Set to None so a new box can be created

        # Reinitialize boxes if all have exited
        if not any(conveyor.box for conveyor in self.interface.conveyors.values()):
            self.interface.reinitialize_boxes()

# Conveyor interface to manage interactions between conveyors
class ConveyorInterface:
    def __init__(self):
        self.boxes = []
        self.conveyors = {}

    def register_conveyor(self, conveyor):
        self.conveyors[conveyor.conveyor_id] = conveyor

    def register_box(self, box):
        self.boxes.append(box)

    def unregister_box(self, box):
        if box in self.boxes:
            self.boxes.remove(box)

    def get_next_priority_box(self, current_priority):
        # Get the next lower-priority box
        lower_priority_boxes = [box for box in self.boxes if box.priority > current_priority]
        if lower_priority_boxes:
            return min(lower_priority_boxes, key=lambda b: b.priority)
        return None

    def reinitialize_boxes(self):
        # Clear all existing boxes
        self.boxes.clear()
        # Reinitialize each conveyor with a new box at a random position
        for conveyor in self.conveyors.values():
            conveyor.initialize_box()
        # Assign new priorities based on proximity to exit
        self.assign_priorities()

    def assign_priorities(self):
        # Sort boxes by distance to the exit and assign priorities
        sorted_boxes = sorted(self.boxes, key=lambda box: box.x_pos + box_size)
        for priority, box in enumerate(sorted_boxes, start=1):
            box.priority = priority
            box.text.set_text(str(box.priority))  # Update the displayed priority

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(0, conveyor_height)
ax.set_ylim(-50, conveyor_height + 50)
ax.axis('on')

# Draw conveyor lane borders
for lane_y in lanes_y:
    ax.plot([0, conveyor_height], [lane_y, lane_y], color='gray', linestyle='-', linewidth=2)

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
        conveyor.update_position()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
