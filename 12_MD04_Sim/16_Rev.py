import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation

# Define conveyor and box parameters
conveyor_length = 30  # Length of conveyor in units
box_width, box_height = 3, 1.5  # Box dimensions
gap = 5  # Required gap between boxes in units

# Box class representing each parcel
class Box:
    def __init__(self, ax, lane_y, initial_x, is_rotated=False):
        self.x_pos = initial_x
        self.lane_y = lane_y
        self.is_rotated = is_rotated
        self.speed = 0.1  # Speed of box movement

        # Calculate center position and rotation
        if is_rotated:
            rotation_angle = np.radians(30)
        else:
            rotation_angle = 0

        # Define box rectangle with rotation
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

    def move(self):
        self.x_pos += self.speed
        translation = np.array([self.x_pos, self.lane_y]) - np.array([self.rect.xy[0, 0], self.rect.xy[0, 1]])
        self.rect.xy += translation

    def get_right_edge(self):
        return np.max(self.rect.xy[:, 0])

    def get_left_edge(self):
        return np.min(self.rect.xy[:, 0])

# Conveyor class to manage movement and gap control
class Conveyor:
    def __init__(self, ax, lane_y, initial_x, is_rotated=False):
        self.box = Box(ax, lane_y, initial_x, is_rotated)
        self.lane_y = lane_y

    def update_position(self):
        self.box.move()

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, conveyor_length + 10)
ax.set_ylim(-2, 14)
ax.axis("on")

# Draw conveyor lane borders
ax.plot([0, conveyor_length + 10], [10, 10], color="black", linewidth=2)
ax.plot([0, conveyor_length + 10], [0, 0], color="black", linewidth=2)

# Create two conveyors with boxes
conveyor1 = Conveyor(ax, 10, 5, is_rotated=False)  # Section 1
conveyor2 = Conveyor(ax, 2, conveyor1.box.get_right_edge() + gap + box_width / 2, is_rotated=True)  # Section 2

# Update function for animation
def update(frame):
    # Update positions of boxes
    conveyor1.update_position()
    conveyor2.update_position()

    # Ensure gap between the right edge of box in Section 1 and left edge of box in Section 2
    if conveyor1.box.get_right_edge() + gap > conveyor2.box.get_left_edge():
        conveyor2.box.speed = 0  # Stop if the gap is less than required
    else:
        conveyor2.box.speed = 0.1  # Move if gap is sufficient

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 300), interval=50, repeat=False)
plt.show()
