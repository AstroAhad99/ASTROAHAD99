import numpy as np
import matplotlib.pyplot as plt

# Define parameters
L_offset = 0.5  # Assumed offset length on conveyor 2 where the box needs to shift (in meters)
box_widths = np.linspace(0.1, 2.0, 100)  # Varying box widths from 0.1 m to 2.0 m

# Calculate roller angle in degrees based on the box width
roller_angles = np.degrees(np.arctan(box_widths / L_offset))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(box_widths, roller_angles, label='Roller Angle (θ) vs Box Width', color='blue')
plt.xlabel('Box Width (m)')
plt.ylabel('Roller Angle θ (degrees)')
plt.title('Roller Angle Required Based on Box Width')
plt.grid(True)
plt.legend()
plt.show()


# Calculate the maximum allowable angle theta for the given max roller speed
v_box = 0.5  # Box speed in m/s
v_roller_max = 1.5  # Max roller speed in m/s

# Calculate the maximum angle theta (in degrees) that keeps roller speed within the max limit
theta_max = np.degrees(np.arccos(v_box / v_roller_max))

# Define angles up to the calculated max angle for plotting
angles_limited = np.linspace(0, theta_max, 100)
roller_speeds_limited = v_box / np.cos(np.radians(angles_limited))  # Calculate roller speeds within the limit

# Plotting roller speed vs roller angle with the limited range
plt.figure(figsize=(10, 6))
plt.plot(angles_limited, roller_speeds_limited, label='Roller Speed (v_roller)', color='blue')
plt.axhline(v_roller_max, color='orange', linestyle='--', label='Max Roller Speed (1.5 m/s)')
plt.xlabel('Roller Angle θ (degrees)')
plt.ylabel('Roller Speed v_roller (m/s)')
plt.title(f'Roller Speed vs Angle (Limited to θ <= {theta_max:.2f} degrees)')
plt.legend()
plt.grid(True)
plt.show()

theta_max

