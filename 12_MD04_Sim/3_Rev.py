import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation

# Define conveyor and box parameters
conveyor_width = 200  # Width of conveyor in pixels
conveyor_height = 600  # Height of conveyor in pixels
box_size = 30  # Size of each box in pixels
gap = 40  # Required gap between tail of one box and head of the next box in pixels
exit_position = 550  # Position where boxes exit the conveyor
lanes = [0, 150, 300, 450]  # Lane y-positions for the 4 conveyors

# Box class representing each parcel
class Box:
    def __init__(self, ax, lane, box_id, initial_x):
        self.lane = lane
        self.box_id = box_id
        self.x_pos = initial_x
        self.rect = patches.Rectangle((self.x_pos, lane), box_size, box_size, linewidth=1, edgecolor='black', facecolor='white')
        self.text = ax.text(self.x_pos + box_size / 4, lane + box_size / 4, str(self.box_id), ha='center', va='center', fontsize=8, color='black')
        ax.add_patch(self.rect)

    def move(self, speed):
        self.x_pos += speed
        self.rect.set_x(self.x_pos)
        self.text.set_x(self.x_pos + box_size / 4)

    def remove(self):
        self.rect.remove()
        self.text.remove()

# Conveyor class to manage all boxes on the conveyor
class Conveyor:
    def __init__(self, ax):
        self.ax = ax
        self.boxes = []
        self.initialize_boxes()

    def initialize_boxes(self):
        minor_offsets = [0, 5, 10, 15]  # Initial slight x-offsets for boxes in each lane
        self.boxes = [Box(self.ax, lane, idx + 1, minor_offsets[idx]) for idx, lane in enumerate(lanes)]

    def update_positions(self):
        # Update the position of each box
        for box in self.boxes:
            if box.x_pos < exit_position:
                # Calculate speed dynamically to maintain the required tail-to-head gap with the next box
                speed = 2
                next_box = self.get_next_box(box)
                
                # Check the distance between the tail of the current box and the head of the next box
                if next_box:
                    distance_to_next_box = next_box.x_pos - (box.x_pos + box_size)
                    if distance_to_next_box < gap:
                        speed = 1  # Slow down if the distance is less than the required gap
                    elif distance_to_next_box > gap:
                        speed = 2  # Speed up if distance is larger than needed to close the gap

                box.move(speed)
            else:
                # Remove the box from the plot if it reaches the exit position
                box.remove()
                self.boxes.remove(box)

        # Reinitialize boxes if all have exited
        if not self.boxes:
            self.initialize_boxes()

    def get_next_box(self, current_box):
        # Find the next box in the same lane that is ahead of the current box
        same_lane_boxes = [box for box in self.boxes if box.lane == current_box.lane and box.x_pos > current_box.x_pos]
        if same_lane_boxes:
            return min(same_lane_boxes, key=lambda b: b.x_pos)
        return None

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(0, conveyor_width)
ax.set_ylim(-50, conveyor_height + 50)
ax.axis('off')

# Draw conveyor lane borders
for lane in lanes:
    ax.plot([0, conveyor_width], [lane, lane], color='gray', linestyle='-', linewidth=2)

# Create a Conveyor object
conveyor = Conveyor(ax)

# Update function for animation
def update(frame):
    conveyor.update_positions()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
