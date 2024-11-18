import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Parameters
conveyor_length = 10  # Length of conveyor 1 in arbitrary units
conveyor_width = 1  # Width of the conveyors
box_size = 0.5  # Size of each box
conveyor_speed = 0.1  # Speed at which the boxes move on conveyor 1
roller_speed = 0.05  # Speed at which the box moves sideways on conveyor 2

# Initialize figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, conveyor_length + 5)
ax.set_ylim(-1, conveyor_length + 5)

# Draw conveyors
ax.plot([0, conveyor_length], [0, 0], 'k-', lw=10)  # Conveyor 1 (horizontal)
ax.plot([conveyor_length, conveyor_length], [0, conveyor_length], 'k-', lw=10)  # Conveyor 3 (vertical)
ax.plot([0, conveyor_length], [conveyor_width, conveyor_width], 'k-', lw=10)  # Conveyor 2 boundary

# Box parameters
boxes = []  # List to store box positions
colors = ['blue', 'green', 'orange']

# Function to add a new box at random intervals
def add_box():
    if random.random() < 0.2:  # 20% chance to add a box each frame
        box = {'x': 0, 'y': 0, 'moving': 'conveyor_1', 'color': random.choice(colors)}
        boxes.append(box)

# Animation update function
def update(frame):
    ax.clear()
    ax.set_xlim(-1, conveyor_length + 5)
    ax.set_ylim(-1, conveyor_length + 5)
    
    # Redraw conveyors
    ax.plot([0, conveyor_length], [0, 0], 'k-', lw=10)  # Conveyor 1
    ax.plot([conveyor_length, conveyor_length], [0, conveyor_length], 'k-', lw=10)  # Conveyor 3
    ax.plot([0, conveyor_length], [conveyor_width, conveyor_width], 'k-', lw=10)  # Conveyor 2 boundary

    # Add a new box at random intervals
    add_box()
    
    # Update each box's position
    for box in boxes:
        if box['moving'] == 'conveyor_1':
            box['x'] += conveyor_speed
            # Check if box reaches the end of conveyor 1
            if box['x'] >= conveyor_length - box_size:
                box['moving'] = 'conveyor_2'  # Move to conveyor 2
        elif box['moving'] == 'conveyor_2':
            box['y'] += roller_speed
            # Check if box reaches the end of conveyor 2 (to conveyor 3)
            if box['y'] >= conveyor_width:
                box['moving'] = 'conveyor_3'  # Move to conveyor 3
        elif box['moving'] == 'conveyor_3':
            box['y'] += conveyor_speed

        # Draw the box
        ax.add_patch(plt.Rectangle((box['x'], box['y']), box_size, box_size, color=box['color'], ec='black'))

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=100)

plt.show()
