import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


# Function to draw a conveyor section with two rectangular boxes
def draw_conveyor_section_two_boxes(ax, section_number, rotation_angle1=0, rotation_angle2=0):
    # Draw conveyor section
    conveyor = patches.Rectangle((0, 0), 20, 4, linewidth=2, edgecolor="black", facecolor="none")
    ax.add_patch(conveyor)
    ax.text(-1, 2, "Entry", va="center", ha="right")
    ax.text(21, 2, "Exit", va="center", ha="left")
    ax.text(10, 4.5, f"Section {section_number}", ha="center", va="center", fontsize=12)

    # Define box dimensions
    box_width, box_height = 3, 1.5  # Rectangular box dimensions

    # Function to get rotated corners and closest/furthest points
    def get_box_properties(center, rotation_angle):
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
        rotated_corners = local_corners.dot(rotation_matrix) + center

        # Find the closest and furthest points to the exit (located at x=20)
        distances = np.linalg.norm(rotated_corners - np.array([20, 2]), axis=1)
        closest_point = rotated_corners[np.argmin(distances)]
        furthest_point = rotated_corners[np.argmax(distances)]
        
        return rotated_corners, closest_point, furthest_point

    # Define initial position for the first box and its rotation
    box1_center = np.array([5, 2])  # Center of the first box
    rotated_corners1, closest_point1, furthest_point1 = get_box_properties(box1_center, rotation_angle1)

    # Calculate the center for the second box with a gap of 5 from the first box's furthest point
    box2_center = furthest_point1 + np.array([5 + box_width / 2, 0])
    rotated_corners2, closest_point2, furthest_point2 = get_box_properties(box2_center, rotation_angle2)

    # Draw first box, closest, and furthest points
    box1 = patches.Polygon(rotated_corners1, closed=True, edgecolor="black", facecolor="lightgrey")
    ax.add_patch(box1)
    ax.plot(*closest_point1, "o", color="red")
    ax.text(closest_point1[0], closest_point1[1] + 0.3, "Closest", color="red", ha="center")
    ax.plot(*furthest_point1, "o", color="blue")
    ax.text(furthest_point1[0], furthest_point1[1] + 0.3, "Furthest", color="blue", ha="center")

    # Draw second box, closest, and furthest points
    box2 = patches.Polygon(rotated_corners2, closed=True, edgecolor="black", facecolor="lightgrey")
    ax.add_patch(box2)
    ax.plot(*closest_point2, "o", color="red")
    ax.text(closest_point2[0], closest_point2[1] + 0.3, "Closest", color="red", ha="center")
    ax.plot(*furthest_point2, "o", color="blue")
    ax.text(furthest_point2[0], furthest_point2[1] + 0.3, "Furthest", color="blue", ha="center")

    # Set limits and labels
    ax.set_xlim(-1, 21)
    ax.set_ylim(-1, 5)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

# Create plot for two boxes in each section with a gap of 5 units
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 14))

# Section 1 (no rotation on both boxes)
draw_conveyor_section_two_boxes(ax1, section_number=1, rotation_angle1=0, rotation_angle2=0)

# Section 2 (rotation on both boxes)
rotation_angle1 = np.radians(30)  # 30 degrees rotation for the first box
rotation_angle2 = np.radians(45)  # 45 degrees rotation for the second box
draw_conveyor_section_two_boxes(ax2, section_number=2, rotation_angle1=rotation_angle1, rotation_angle2=rotation_angle2)

plt.show()
