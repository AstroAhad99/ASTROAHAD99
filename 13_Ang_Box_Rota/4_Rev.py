# Re-import necessary libraries due to execution context reset
import numpy as np
import matplotlib.pyplot as plt

# Define parameters for gradual angle increase
L1 = 10.0  # Length of conveyor 1 (in meters)
T = 9.0  # Threshold position (90% of conveyor 1 length)
P = np.linspace(0, L1, 200)  # Box positions along conveyor 1 (tracking of box on MD05)
W = 1.0  # Box width (in meters) (input the width of the box)
L_offset = 0.1  # Effective length offset for angle calculation
theta_final = np.degrees(np.arctan(W / L_offset))  # Final roller angle for 1m box

# Linear gradual angle function
theta_linear = np.where(P >= T, theta_final * (P - T) / (L1 - T), 0)

# Sigmoid gradual angle function (non-linear)
k = 6  # Steepness factor for sigmoid
theta_sigmoid = theta_final / (1 + np.exp(-k * (P - T)))

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(P, theta_linear, label="Linear Gradual Angle", color="blue")
plt.plot(P, theta_sigmoid, label="Sigmoid Gradual Angle", color="red")
plt.axvline(T, color="green", linestyle="--", label="Threshold Position (T)")
plt.xlabel("Position on Conveyor 1 (m)")
plt.ylabel("Roller Angle θ (degrees)")
plt.title("Gradual Increase in Roller Angle Based on Box Position")
plt.grid(True)
plt.legend()
plt.show()
