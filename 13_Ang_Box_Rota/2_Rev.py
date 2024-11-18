# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define initial parameters
L_offset = 0.5  # Assumed offset length on conveyor 2 (in meters)
box_widths = np.linspace(0.1, 2.0, 100)  # Varying box widths from 0.1 m to 2.0 m
v_box = 0.5  # Box speed in m/s
v_roller_max = 1.5  # Max roller speed in m/s

# Step 1: Calculate roller angle based on box width
roller_angles = np.degrees(np.arctan(box_widths / L_offset))

# Step 2: Calculate roller speed based on roller angle (limit speed to max roller speed)
roller_speeds = np.minimum(v_box / np.cos(np.radians(roller_angles)), v_roller_max)

# Plotting Roller Angle vs Box Width
plt.figure(figsize=(10, 6))
plt.plot(box_widths, roller_angles, label='Roller Angle (θ) vs Box Width', color='blue')
plt.xlabel('Box Width (m)')
plt.ylabel('Roller Angle θ (degrees)')
plt.title('Roller Angle Required Based on Box Width')
plt.grid(True)
plt.legend()
plt.show()

# Plotting Roller Speed vs Box Width (using calculated angles)
plt.figure(figsize=(10, 6))
plt.plot(box_widths, roller_speeds, label='Roller Speed (v_roller)', color='green')
plt.axhline(v_roller_max, color='orange', linestyle='--', label='Max Roller Speed (1.5 m/s)')
plt.xlabel('Box Width (m)')
plt.ylabel('Roller Speed v_roller (m/s)')
plt.title('Roller Speed Based on Box Width (Limited by Max Roller Speed)')
plt.legend()
plt.grid(True)
plt.show()
