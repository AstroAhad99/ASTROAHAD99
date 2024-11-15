import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import numpy as np
from matplotlib.animation import FuncAnimation

# Define the conveyor dimensions and parameters
conveyor_width = 200  # pixels
conveyor_height = 600  # pixels (4 lanes each 150 pixels in width)
box_size = 30  # pixels for each box
gap = 50  # pixel gap between exiting boxes
exit_position = 550  # exit position in the x direction

# Conveyor lanes (y positions for each of the 4 lanes)
lanes = [0, 150, 300, 450]

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, conveyor_width)
ax.set_ylim(-50, conveyor_height + 50)  # Extra space for exit visualization
ax.axis('off')

# List to store boxes
boxes = []
box_speeds = []


# Initialize box creation and parameters
def create_box():
    lane = random.choice(lanes)
    id_num = len(boxes) + 1
    rect = patches.Rectangle((0, lane), box_size, box_size, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(rect)
    boxes.append({'rect': rect, 'lane': lane, 'id': id_num, 'x_pos': 0})


# Update function for animation
def update(frame):
    # Add a new box randomly
    if random.random() < 0.1:
        create_box()

    # Move each box to the right at its speed
    for box in boxes:
        if box['x_pos'] < exit_position:
            # Move box to the right
            box['x_pos'] += 2  # Fixed speed for simplicity
            box['rect'].set_x(box['x_pos'])
        else:
            # Remove the box from the plot if it reaches the exit
            box['rect'].remove()
            boxes.remove(box)

    # Display ID on each box
    for box in boxes:
        if 'text' in box:
            box['text'].remove()
        box['text'] = ax.text(box['x_pos'] + box_size / 4, box['lane'] + box_size / 4,
                              str(box['id']), ha='center', va='center', fontsize=8, color='black')


# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
