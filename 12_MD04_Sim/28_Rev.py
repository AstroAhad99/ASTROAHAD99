import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation
import random

# Define conveyor and box parameters
conveyor_width = 200  # Width of conveyor in pixels
conveyor_height = 600  # Height of conveyor in pixels
exit_position = 600  # Position where boxes exit the conveyor
lanes_y = [0, 150, 300, 450]  # Y-positions for each lane
gap = 40  # Required gap between tail of one box and head of the next box in pixels

# Box class representing each parcel
class Box:
    def __init__(self, ax, lane_y, box_id, initial_x, priority, width, height):
        self.ax = ax
        self.lane_y = lane_y
        self.box_id = box_id
        self.priority = priority
        self.x_pos = initial_x
        self.left_edge = 0
        self.right_edge = 0
        self.width = width
        self.height = height
        self.rotation_angle = np.radians(random.uniform(0, 0))
        self.speed = 2  # Initial speed
        self.create_box()

    def __repr__(self):
        return (f"Priority={self.priority}, X_pos={self.x_pos}")

    def create_box(self):
    # Calculate the rotated corners of the box
        self.corners = np.array([
            [-self.width / 2, -self.height / 2],
            [self.width / 2, -self.height / 2],
            [self.width / 2, self.height / 2],
            [-self.width / 2, self.height / 2]
        ])
        rotation_matrix = np.array([
            [np.cos(self.rotation_angle), -np.sin(self.rotation_angle)],
            [np.sin(self.rotation_angle), np.cos(self.rotation_angle)]
        ])
        centered_y = self.lane_y + (150 - self.height) / 2
        rotated_corners = self.corners.dot(rotation_matrix) + [self.x_pos, self.lane_y]
        self.rect = patches.Polygon(rotated_corners, closed=True, edgecolor="black", facecolor="lightgrey")
        self.text = ax.text(self.x_pos + self.width / 4, centered_y + self.height / 4, str(self.priority),
                        ha='center', va='center', fontsize=8, color='black')
        self.ax.add_patch(self.rect)

        # Marking left and right edges as points
        self.left_edge_marker, = self.ax.plot([], [], 'bo', label="Left Edge")
        self.right_edge_marker, = self.ax.plot([], [], 'ro', label="Right Edge")
        self.update_edge_markers()

    def move(self):
        self.x_pos += self.speed
        translation = np.array([self.x_pos, self.lane_y]) - np.array([self.rect.xy[0, 0], self.rect.xy[0, 1]])
        self.rect.xy += translation
        self.text.set_x(self.x_pos + self.width / 4)
        self.update_edge_markers()

    def get_right_edge(self):
        self.right_edge = np.max(self.rect.xy[:, 0])
        return self.right_edge

    def get_left_edge(self):
        self.left_edge = np.min(self.rect.xy[:, 0])
        return self.left_edge

    def update_edge_markers(self):
        left_edge_x = self.get_left_edge()
        right_edge_x = self.get_right_edge()
        self.left_edge_marker.set_data([left_edge_x], [self.lane_y])
        self.right_edge_marker.set_data([right_edge_x], [self.lane_y])

    def remove(self):
        self.rect.remove()
        self.text.remove()
        self.left_edge_marker.remove()
        self.right_edge_marker.remove()

# Conveyor class to manage a single box on a single lane
class Conveyor:
    def __init__(self, ax, lane_y, conveyor_id, interface, box):
        self.ax = ax
        self.lane_y = lane_y
        self.conveyor_id = conveyor_id
        self.interface = interface  # Interface to interact with other conveyors
        self.box = box  # Initialize without a box

    def update_position(self):
        if self.box:
            if self.box.get_right_edge() < exit_position:
                # Get the next lower-priority box
                next_box = self.interface.get_next_priority_box(self.box.priority)

                # Adjust speed based on the gap requirement with the next lower-priority box
                if next_box:
                    distance_to_next_box = next_box.get_left_edge() - self.box.get_right_edge()
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
#            self.interface.reinitialize_boxes()
            Builder.has_run = False

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

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-100, conveyor_height)
ax.set_ylim(-100, conveyor_height + 100)
ax.axis('on')

def Builder():

    if getattr(Builder, 'has_run', False):
        print("This function has already run.")
        return
    print("Running the function...")

    x_positions = [random.randint(50, 100) for pos in range(0,4)]
    lanes_y = [0, 150, 300, 450]  # Y-positions for each lane
    conveyor_id = [1, 2, 3, 4]
    widths = [random.randint(10, 30) for wid in range(0,4)]
    heights = [random.randint(30, 40) for hei in range(0,4)]
    priority = []
    make_boxes = [Box(ax, lanes_y[pos], conveyor_id[pos], x_positions[pos], 0, widths[pos], heights[pos]) for pos in range(0, 4)]
    distances = []

    for index, value in enumerate(make_boxes):
        left_edge = abs(value.get_left_edge())
        right_edge = abs(value.get_right_edge())
        print(left_edge, right_edge)
        dist = conveyor_height - x_positions[index] + (right_edge - left_edge)
        distances.append(dist)

    # Sorting the list while keeping track of indices
    sorted_indices = sorted(range(len(distances)), key=lambda x: distances[x])

    # Create the priority list with default value 0
    priority = [0] * len(distances)

    # Assign priorities based on the sorted indices
    for rank, index in enumerate(sorted_indices, start=1):
        priority[index] = len(distances) - rank + 1
    print(distances)
    print(priority)
    final_boxes = [Box(ax, lanes_y[pos], conveyor_id[pos], x_positions[pos], priority[pos], widths[pos], heights[pos]) for pos in range(0, 4)]
    return final_boxes


builder = Builder()


# Draw conveyor lane borders
for lane_y in lanes_y:
    ax.plot([-100, conveyor_height], [lane_y, lane_y], color='gray', linestyle='-', linewidth=2)

# Create ConveyorInterface and Conveyor objects
interface = ConveyorInterface()
conveyors = []
for idx, lane_y in enumerate(lanes_y):
    Builder.has_run = True
    conveyor = Conveyor(ax, lane_y, idx, interface, builder[idx])
    interface.register_box(builder[idx])
    conveyors.append(conveyor)
    interface.register_conveyor(conveyor)

# Update function for animation
def update(frame):
    for conveyor in conveyors:
        conveyor.update_position()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
