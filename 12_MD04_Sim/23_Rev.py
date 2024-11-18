import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation
import random

# Define conveyor parameters
conveyor_length = 30  # Length of conveyor in units
gap = 5  # Required gap between boxes in units
exit_position = conveyor_length + 5  # Position where boxes exit the conveyor

# Box class representing each parcel with edge markers
class BoxWithEdges:
    def __init__(self, ax, lane_y, initial_x):
        self.ax = ax
        self.x_pos = initial_x
        self.lane_y = lane_y
        self.width = random.uniform(3, 6)  # Random width between 3 and 6
        self.height = random.uniform(1.5, 3)  # Random height between 1.5 and 3
        self.rotation_angle = np.radians(random.uniform(0, 360))  # Random rotation angle between 0 and 360 degrees
        self.speed = 0.05  # Initial slow speed to create gap
        self.create_box()

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
        rotated_corners = self.corners.dot(rotation_matrix) + [self.x_pos, self.lane_y]
        self.rect = patches.Polygon(rotated_corners, closed=True, edgecolor="black", facecolor="lightgrey")
        self.ax.add_patch(self.rect)

        # Marking left and right edges as points
        self.left_edge_marker, = self.ax.plot([], [], 'bo', label="Left Edge")
        self.right_edge_marker, = self.ax.plot([], [], 'ro', label="Right Edge")
        self.update_edge_markers()

    def move(self):
        self.x_pos += self.speed
        translation = np.array([self.x_pos, self.lane_y]) - np.array([self.rect.xy[0, 0], self.rect.xy[0, 1]])
        self.rect.xy += translation
        self.update_edge_markers()

    def get_right_edge(self):
        return np.max(self.rect.xy[:, 0])

    def get_left_edge(self):
        return np.min(self.rect.xy[:, 0])

    def update_edge_markers(self):
        left_edge_x = self.get_left_edge()
        right_edge_x = self.get_right_edge()
        self.left_edge_marker.set_data([left_edge_x], [self.lane_y])
        self.right_edge_marker.set_data([right_edge_x], [self.lane_y])

    def remove(self):
        self.rect.remove()
        self.left_edge_marker.remove()
        self.right_edge_marker.remove()

# Conveyor class that manages box movement and gap maintenance with priority
class ConveyorWithEdgeMarkers:
    def __init__(self, ax, lane_y, initial_x, priority, paired_conveyor=None, interface=None):
        self.ax = ax
        self.lane_y = lane_y
        self.priority = priority  # Priority of this conveyor's box
        self.paired_conveyor = paired_conveyor
        self.interface = interface
        self.box = BoxWithEdges(ax, lane_y, initial_x)
        self.gap_created = False

    def update_position(self):
        if self.box:
            # If box hasn't exited, manage gap and speed
            if self.box.get_right_edge() < exit_position:
                # Check the gap and speed based on priority
                if self.paired_conveyor:
                    if self.priority < self.paired_conveyor.priority:
                        # This box has lower priority; it should adjust speed to maintain gap
                        distance_to_paired_box = self.paired_conveyor.box.get_left_edge() - self.box.get_right_edge()
                        if distance_to_paired_box < gap:
                            self.box.speed = 0.05  # Slow down if the gap is less than required
                        else:
                            self.box.speed = 0.1  # Speed up if the gap is sufficient
                            self.gap_created = True
                    else:
                        # This box has higher priority; it should move ahead to create the gap
                        self.box.speed = 0.1
                else:
                    # No paired conveyor, maintain constant speed
                    self.box.speed = 0.1
                self.box.move()
            else:
                # Remove the box if it reaches the exit
                self.box.remove()
                self.interface.unregister_box(self.box)
                self.box = None

# ConveyorInterface to manage interactions between conveyors and handle reinitialization
class ConveyorInterface:
    def __init__(self, ax):
        self.ax = ax
        self.conveyors = []
        self.boxes = []

    def add_conveyor(self, conveyor):
        self.conveyors.append(conveyor)

    def register_box(self, box):
        self.boxes.append(box)

    def unregister_box(self, box):
        if box in self.boxes:
            self.boxes.remove(box)

    def reinitialize_boxes(self):
        initial_x_position = 0  # Set to 0 to start at the beginning of the conveyor
        # Assign random priorities to the boxes for each reinitialization
        priority1, priority2 = random.sample([1, 2], 2)  # Assign unique priorities
        # Reinitialize both boxes with random sizes, rotation angles, and reset speed control
        self.conveyors[0].box = BoxWithEdges(self.ax, 10, initial_x_position)
        self.conveyors[0].priority = priority1
        self.conveyors[1].box = BoxWithEdges(self.ax, 0, initial_x_position)
        self.conveyors[1].priority = priority2
        self.conveyors[0].gap_created = False
        self.conveyors[1].gap_created = False
        self.register_box(self.conveyors[0].box)
        self.register_box(self.conveyors[1].box)

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, conveyor_length)
ax.set_ylim(-5, 15)
ax.axis("on")

# Draw conveyor lane borders
ax.plot([0, conveyor_length + 10], [10, 10], color="black", linewidth=2)
ax.plot([0, conveyor_length + 10], [0, 0], color="black", linewidth=2)

# Create ConveyorInterface and conveyors with initial priorities
interface = ConveyorInterface(ax)
conveyor1 = ConveyorWithEdgeMarkers(ax, 10, 0, priority=1, interface=interface)  # Section 1
conveyor2 = ConveyorWithEdgeMarkers(ax, 0, 0, priority=2, paired_conveyor=conveyor1, interface=interface)  # Section 2
interface.add_conveyor(conveyor1)
interface.add_conveyor(conveyor2)
interface.register_box(conveyor1.box)
interface.register_box(conveyor2.box)

# Update function for animation
def update(frame):
    conveyor1.update_position()
    conveyor2.update_position()

    # Check if all boxes have exited and reinitialize if needed
    if not any(conveyor.box for conveyor in interface.conveyors):
        interface.reinitialize_boxes()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 300), interval=50)
plt.show()
