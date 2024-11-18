import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Function to draw a conveyor section and box
def draw_conveyor_section(ax, section_number, rotation_angle=0):
    # Draw conveyor section
    conveyor = patches.Rectangle((0, 0), 10, 4, linewidth=2, edgecolor="black", facecolor="none")
    ax.add_patch(conveyor)
    ax.text(-1, 2, "Entry", va="center", ha="right")
    ax.text(11, 2, "Exit", va="center", ha="left")
    ax.text(5, 4.5, f"Section {section_number}", ha="center", va="center", fontsize=12)

    # Define box dimensions and position
    box_center = np.array([3, 2])  # Center of the box
    box_width, box_height = 2, 2  # Box dimensions

    # Box corners in local coordinates
    local_corners = np.array([
        [-box_width / 2, -box_height / 2],
        [box_width / 2, -box_height / 2],
        [box_width / 2, box_height / 2],
        [-box_width / 2, box_height / 2]
    ])

    # Rotate corners
    rotation_matrix = np.array([
        [np.cos(rotation_angle), -np.sin(rotation_angle)],
        [np.sin(rotation_angle), np.cos(rotation_angle)]
    ])
    rotated_corners = local_corners.dot(rotation_matrix) + box_center

    # Find the closest point to the exit (located at x=10)
    distances = np.linalg.norm(rotated_corners - np.array([10, 2]), axis=1)
    closest_point = rotated_corners[np.argmin(distances)]

    # Draw box and closest point
    box = patches.Polygon(rotated_corners, closed=True, edgecolor="black", facecolor="lightgrey")
    ax.add_patch(box)
    ax.plot(*closest_point, "o", color="red", label="Closest Point to Exit")
    ax.text(closest_point[0], closest_point[1] + 0.3, "Closest", color="red", ha="center")

    # Set limits and labels
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 5)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

# Create plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

# Section 1 (no rotation)
draw_conveyor_section(ax1, section_number=1, rotation_angle=0)

# Section 2 (with rotation)
rotation_angle = np.radians(30)  # 30 degrees rotation
draw_conveyor_section(ax2, section_number=2, rotation_angle=rotation_angle)

plt.show()
