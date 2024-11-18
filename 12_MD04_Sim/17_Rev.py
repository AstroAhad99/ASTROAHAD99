import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation
import random

# Define conveyor and box parameters
conveyor_length = 30  # Length of conveyor in units
conveyor_height = 4   # Height of conveyor in units
lanes_y = [0, 4, 8, 12]  # Y-positions for each conveyor lane
initial_gap = 5  # Required gap between boxes

# Box class representing each parcel
class Box:
    def __init__(self, ax, lane_y, box_id, initial_x, priority):
        self.lane_y = lane_y
        self.box_id = box_id
        self.priority = priority
        self.x_pos = initial_x
        self.width = random.uniform(2.5, 3.5)  # Random width within a specified range
        self.height = 1.5  # Height of each box
        self.speed = 1  # Initial speed

        # Randomly decide if box is rotated
        self.is_rotated = random.choice([True, False])
        rotation_angle = np.radians(30) if self.is_rotated else 0

        # Set up box corners and rotation
        self.corners = np.array([
            [-self.width / 2, -self.height / 2],
            [self.width / 2, -self.height / 2],
            [self.width / 2, self.height / 2],
            [-self.width / 2, self.height / 2]
        ])
        rotation_matrix = np.array([
            [np.cos(rotation_angle), -np.sin(rotation_angle)],
            [np.sin(rotation_angle), np.cos(rotation_angle)]
        ])
        rotated_corners = self.corners.dot(rotation_matrix) + [self.x_pos, self.lane_y]
        self.rect = patches.Polygon(rotated_corners, closed=True, edgecolor="black", facecolor="lightgrey")
        ax.add_patch(self.rect)

    def move(self):
        self.x_pos += self.speed
        translation = np.array([self.x_pos, self.lane_y]) - np.array([self.rect.xy[0, 0], self.rect.xy[0, 1]])
        self.rect.xy += translation

    def get_right_edge(self):
        return np.max(self.rect.xy[:, 0])

    def get_left_edge(self):
        return np.min(self.rect.xy[:, 0])

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
        # Create a new box with a random starting position
        initial_x = random.randint(0, 15)
        self.box = Box(self.ax, self.lane_y, self.conveyor_id + 1, initial_x, 0)  # Priority will be set later
        self.interface.register_box(self.box)
        self.interface.assign_priorities()  # Assign initial priorities based on distance to exit

    def update_position(self):
        if self.box:
            # Get the next lower-priority box
            next_box = self.interface.get_next_priority_box(self.box.priority)

            # Adjust speed based on the gap requirement with the next lower-priority box
            if next_box:
                distance_to_next_box = next_box.get_left_edge() - self.box.get_right_edge()
                if distance_to_next_box < initial_gap:
                    self.box.speed = 1  # Slow down if the distance is less than the gap
                else:
                    self.box.speed = 2  # Speed up if distance is sufficient

            # Move the box
            self.box.move()

# Conveyor interface to manage interactions between conveyors
class ConveyorInterface:
    def __init__(self):
        self.boxes = []
        self.conveyors = {}

    def register_conveyor(self, conveyor):
        self.conveyors[conveyor.conveyor_id] = conveyor

    def register_box(self, box):
        self.boxes.append(box)

    def get_next_priority_box(self, current_priority):
        # Get the next lower-priority box
        lower_priority_boxes = [box for box in self.boxes if box.priority > current_priority]
        if lower_priority_boxes:
            return min(lower_priority_boxes, key=lambda b: b.priority)
        return None

    def assign_priorities(self):
        # Sort boxes by distance to the conveyor exit and assign priorities
        sorted_boxes = sorted(self.boxes, key=lambda box: conveyor_length - box.get_right_edge())
        for priority, box in enumerate(sorted_boxes, start=1):
            box.priority = priority

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, conveyor_length + 5)
ax.set_ylim(-2, conveyor_height * 4 + 2)
ax.axis('on')

# Draw conveyor lane borders
for lane_y in lanes_y:
    ax.plot([0, conveyor_length + 5], [lane_y, lane_y], color='black', linewidth=2)

# Create ConveyorInterface and Conveyor objects
interface = ConveyorInterface()
conveyors = []
for idx, lane_y in enumerate(lanes_y):
    conveyor = Conveyor(ax, lane_y + conveyor_height / 2, idx, interface)
    conveyors.append(conveyor)
    interface.register_conveyor(conveyor)

# Update function for animation
def update(frame):
    for conveyor in conveyors:
        conveyor.update_position()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 300), interval=50, repeat=False)
plt.show()
