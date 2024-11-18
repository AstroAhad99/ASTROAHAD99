import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation

# Redefine parameters for the conveyor and boxes
conveyor_length = 30  # Length of conveyor in units
box_width, box_height = 3, 1.5  # Box dimensions
gap = 5  # Required gap between boxes in units

# Modifying the BoxWithDynamicSpeed class to mark left and right edges of both boxes
class BoxWithEdges:
    def __init__(self, ax, lane_y, initial_x, is_rotated=False):
        self.x_pos = initial_x
        self.lane_y = lane_y
        self.is_rotated = is_rotated
        self.speed = 0.05  # Initial slow speed to create gap

        # Rotation setup
        rotation_angle = np.radians(30) if is_rotated else 0
        self.corners = np.array([
            [-box_width / 2, -box_height / 2],
            [box_width / 2, -box_height / 2],
            [box_width / 2, box_height / 2],
            [-box_width / 2, box_height / 2]
        ])
        rotation_matrix = np.array([
            [np.cos(rotation_angle), -np.sin(rotation_angle)],
            [np.sin(rotation_angle), np.cos(rotation_angle)]
        ])
        rotated_corners = self.corners.dot(rotation_matrix) + [self.x_pos, self.lane_y]
        self.rect = patches.Polygon(rotated_corners, closed=True, edgecolor="black", facecolor="lightgrey")
        ax.add_patch(self.rect)

        # Marking left and right edges as points
        self.left_edge_marker, = ax.plot([], [], 'bo', label="Left Edge")
        self.right_edge_marker, = ax.plot([], [], 'ro', label="Right Edge")
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
        # Update the marker positions for left and right edges
        left_edge_x = self.get_left_edge()
        right_edge_x = self.get_right_edge()
        self.left_edge_marker.set_data([left_edge_x], [self.lane_y])
        self.right_edge_marker.set_data([right_edge_x], [self.lane_y])


# Redefine the Conveyor class to use BoxWithEdges
class ConveyorWithEdgeMarkers:
    def __init__(self, ax, lane_y, initial_x, is_rotated=False, paired_conveyor=None):
        self.box = BoxWithEdges(ax, lane_y, initial_x, is_rotated)
        self.lane_y = lane_y
        self.paired_conveyor = paired_conveyor  # The conveyor this one needs to maintain a gap from
        self.gap_created = False

    def update_position(self):
        if self.paired_conveyor and not self.gap_created:
            # Check the current distance to paired box
            distance_to_paired_box = self.paired_conveyor.box.get_right_edge() - self.box.get_left_edge()
            if distance_to_paired_box < gap:
                # Slow down if the gap is less than required
                self.box.speed = 0.05
            else:
                # Speed up if the gap is sufficient and mark gap as created
                self.box.speed = 0.1
                self.gap_created = True
        else:
            # Maintain consistent speed once the gap is created
            self.box.speed = 0.1
            
        self.box.move()

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, conveyor_length + 10)
ax.set_ylim(-2, 14)
ax.axis("on")

# Draw conveyor lane borders
ax.plot([0, conveyor_length + 10], [10, 10], color="black", linewidth=2)
ax.plot([0, conveyor_length + 10], [0, 0], color="black", linewidth=2)

# Create two conveyors with boxes initialized at the same position
initial_x_position = 5
conveyor1 = ConveyorWithEdgeMarkers(ax, 10, initial_x_position, is_rotated=False)  # Section 1
conveyor2 = ConveyorWithEdgeMarkers(ax, 2, initial_x_position, is_rotated=True, paired_conveyor=conveyor1)  # Section 2

# Update function for animation
def update(frame):
    conveyor1.update_position()
    conveyor2.update_position()

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 300), interval=50, repeat=False)
plt.legend(["Left Edge", "Right Edge"], loc="upper right")
plt.show()
