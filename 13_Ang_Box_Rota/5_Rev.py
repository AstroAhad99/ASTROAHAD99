import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
# Define parameters for conveyors and box
conveyor_width = 2  # Width of conveyors (in meters)
conveyor_height = 10  # Height of Conveyor 3 (in meters)
L1 = 10.0  # Length of Conveyor 1 (in meters)
T = 9.0  # Threshold position where rollers start rotating
W = 1.0  # Box width (in meters)
H = 1.0  # Box height (in meters)
L_offset = 1.0  # Effective offset length for angle calculation
theta_final = np.degrees(np.arctan(W / L_offset))  # Final roller angle
roller_angle = 0  # Initial roller angle

# Initialize figure
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2, 12)  # X-axis limits for conveyor visualization
ax.set_ylim(-2, 12)  # Y-axis limits for conveyor visualization

# Conveyor layout
ax.plot([0, 10], [0, 0], 'k-', lw=4, label='Conveyor 1')  # Conveyor 1 (horizontal)
ax.plot([5, 5], [0, 10], 'k-', lw=4, label='Conveyor 3')  # Conveyor 3 (vertical)
ax.plot([0, -5], [0, 0], 'k-', lw=4, label='Conveyor 4')  # Conveyor 4 (horizontal)
ax.plot([0, 5], [0, -5], 'k-', lw=4, label='Conveyor 2')  # Conveyor 2 (rotating)

# Box
box = plt.Rectangle((0, 0), W, H, color='blue', label='Box')
ax.add_patch(box)

# Gradual angle transition (sigmoid-based)
k = 5  # Steepness factor for sigmoid
def calculate_roller_angle(position):
    if position < T:
        return 0
    return theta_final / (1 + np.exp(-k * (position - T)))

# Update function for animation
def update(frame):
    global roller_angle
    x, y = box.get_xy()  # Current box position

    # Move box along Conveyor 1
    if x + W < 10 and roller_angle == 0:
        box.set_xy((x + 0.1, 0))
    # Rotate rollers and move box onto Conveyor 2
    elif x + W >= 10 and y + H <= 0:
        roller_angle = calculate_roller_angle(x + W)
        dx = -0.1 * np.sin(np.radians(roller_angle))
        dy = 0.1 * np.cos(np.radians(roller_angle))
        box.set_xy((x + dx, y + dy))
    # Move box onto Conveyor 3
    elif y + H < 10:
        box.set_xy((5 - W / 2, y + 0.1))
    else:
        pass  # Stop when box reaches Conveyor 3

    return box,

# Animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=True)

plt.legend()
plt.title("Conveyor System with Gradual Roller Angle Transition")
plt.show()
