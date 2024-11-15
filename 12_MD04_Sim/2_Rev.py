# Re-import necessary libraries and re-run the corrected code with conveyor lane borders and enforced gap.

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import numpy as np
from matplotlib.animation import FuncAnimation

# Define the conveyor dimensions and parameters
conveyor_width = 200  # pixels
conveyor_height = 600  # pixels (4 lanes each 150 pixels in width)
box_size = 30  # pixels for each box
gap = 10 + box_size  # pixel gap (10 pixels plus box size)
exit_position = 550  # exit position in the x direction

# Conveyor lanes (y positions for each of the 4 lanes)
lanes = [0, 150, 300, 450]

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, conveyor_width)
ax.set_ylim(-50, conveyor_height + 50)  # Extra space for exit visualization
ax.axis('off')

# Draw conveyor lane borders
for lane in lanes:
    ax.plot([0, conveyor_width], [lane, lane], color='gray', linestyle='-', linewidth=2)

# Updating the code to add a feature that initializes four boxes at once with minor x-position differences
# and moves them along the conveyor, maintaining the gap with boxes in adjacent lanes.

# Reset box list for a fresh start
boxes = []

# Define the gap size for x-direction (between lanes) and initialize minor offsets
minor_offset = [0, 5, 10, 15]  # Slight differences in x-position for initial arrangement

# Function to initialize four boxes at once with minor x differences
def initialize_boxes():
    for i, lane in enumerate(lanes):
        id_num = i + 1
        initial_x_pos = minor_offset[i]
        rect = patches.Rectangle((initial_x_pos, lane), box_size, box_size, linewidth=1, edgecolor='black', facecolor='white')
        ax.add_patch(rect)
        boxes.append({'rect': rect, 'lane': lane, 'id': id_num, 'x_pos': initial_x_pos})

# Initialize the four boxes for the first set
initialize_boxes()

# Update function for animation with gap enforcement between boxes in all lanes
def update(frame):
    # Move each box to the right, enforcing gap between parcels
    for box in boxes:
        if box['x_pos'] < exit_position:
            # Check if there's enough gap with the box in front on the same lane
            next_box_same_lane = min([b for b in boxes if b['lane'] == box['lane'] and b['x_pos'] > box['x_pos']],
                                     key=lambda b: b['x_pos'], default=None)
            # Check if there's enough gap with boxes in adjacent lanes
            adjacent_lanes = [l for l in lanes if l != box['lane']]
            next_box_adjacent_lane = min([b for b in boxes if b['lane'] in adjacent_lanes and b['x_pos'] > box['x_pos']],
                                         key=lambda b: b['x_pos'], default=None)
            
            # Move only if the gap condition is met on both same and adjacent lanes
            if ((next_box_same_lane is None or next_box_same_lane['x_pos'] - box['x_pos'] > gap) and
                (next_box_adjacent_lane is None or next_box_adjacent_lane['x_pos'] - box['x_pos'] > gap)):
                box['x_pos'] += 2  # Move box to the right
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

    # Reinitialize boxes when all are exited
    if not boxes:
        initialize_boxes()

# Re-create the plot for clarity
fig, ax = plt.subplots()
ax.set_xlim(0, conveyor_width)
ax.set_ylim(-50, conveyor_height + 50)  # Extra space for exit visualization
ax.axis('off')

# Draw conveyor lane borders
for lane in lanes:
    ax.plot([0, conveyor_width], [lane, lane], color='gray', linestyle='-', linewidth=2)

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
