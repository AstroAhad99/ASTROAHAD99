import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Function to draw conveyors with a horizontal gap demonstration between the boxes themselves, not the points
def draw_horizontal_gap_connected_conveyors_between_boxes(ax):
    # Draw the first conveyor
    conveyor1 = patches.Rectangle((0, 8), 30, 4, linewidth=2, edgecolor="black", facecolor="none")
    ax.add_patch(conveyor1)
    ax.text(-1, 10, "Entry", va="center", ha="right")
    ax.text(31, 10, "Exit", va="center", ha="left")
    ax.text(15, 13, "Section 1", ha="center", va="center", fontsize=12)

    # Draw the second conveyor below the first one
    conveyor2 = patches.Rectangle((0, 0), 30, 4, linewidth=2, edgecolor="black", facecolor="none")
    ax.add_patch(conveyor2)
    ax.text(-1, 2, "Entry", va="center", ha="right")
    ax.text(31, 2, "Exit", va="center", ha="left")
    ax.text(15, 5, "Section 2", ha="center", va="center", fontsize=12)

    # Define box dimensions
    box_width, box_height = 3, 1.5  # Rectangular box dimensions

    # Function to draw a box and return its outline (left and right edges)
    def get_box_outline(center, rotation_angle):
        # Create local box corner coordinates
        local_corners = np.array([
            [-box_width / 2, -box_height / 2],
            [box_width / 2, -box_height / 2],
            [box_width / 2, box_height / 2],
            [-box_width / 2, box_height / 2]
        ])

        # Rotation matrix
        rotation_matrix = np.array([
            [np.cos(rotation_angle), -np.sin(rotation_angle)],
            [np.sin(rotation_angle), np.cos(rotation_angle)]
        ])
        rotated_corners = local_corners.dot(rotation_matrix) + center

        # Draw the box
        box = patches.Polygon(rotated_corners, closed=True, edgecolor="black", facecolor="lightgrey")
        ax.add_patch(box)

        # Find the left and right edges for gap calculation
        left_edge = np.min(rotated_corners[:, 0])
        right_edge = np.max(rotated_corners[:, 0])
        return left_edge, right_edge

    # Define center for the first box on Conveyor 1
    box1_center = np.array([8, 10])
    left_edge1, right_edge1 = get_box_outline(box1_center, 0)

    # Define center for the second box on Conveyor 2 such that there's a horizontal gap of 5 units between boxes
    box2_center_x = right_edge1 + 5 + box_width / 2  # Adding half the width to center the box
    box2_center = np.array([box2_center_x, 2])
    left_edge2, right_edge2 = get_box_outline(box2_center, np.radians(30))

    # Draw the orange lines and arrows for the horizontal gap between boxes
    gap_line_y = 6  # Gap line position between the conveyors
    ax.plot([right_edge1, right_edge1], [gap_line_y - 0.5, gap_line_y + 0.5], linestyle="-", color="orange", linewidth=2)
    ax.plot([left_edge2, left_edge2], [gap_line_y - 0.5, gap_line_y + 0.5], linestyle="-", color="orange", linewidth=2)
    ax.arrow(right_edge1, gap_line_y, 2.5, 0, head_width=0.2, head_length=0.5, fc="orange", ec="orange")
    ax.arrow(left_edge2, gap_line_y, -2.5, 0, head_width=0.2, head_length=0.5, fc="orange", ec="orange")
    ax.text((right_edge1 + left_edge2) / 2, gap_line_y + 0.3, "gap = 5", color="orange", ha="center", fontsize=10)

    # Set limits and labels
    ax.set_xlim(-1, 31)
    ax.set_ylim(-1, 15)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

# Create plot for conveyors with a horizontal gap demonstration between the boxes
fig, ax = plt.subplots(figsize=(12, 8))

# Draw the connected conveyors with visual elements for a horizontal gap of 5 units between boxes
draw_horizontal_gap_connected_conveyors_between_boxes(ax)

plt.show()
