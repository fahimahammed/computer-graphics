import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up the parameters
a = 100  # x-axis radius
b = 100  # y-axis radius
n = 0.5  # exponent

# Generate the points of the superellipse
theta = np.linspace(0, 2 * np.pi, 100)
x = a * np.sign(np.cos(theta)) * np.power(np.abs(np.cos(theta)), 2/n)
y = b * np.sign(np.sin(theta)) * np.power(np.abs(np.sin(theta)), 2/n)

# Generate the 3D points of the superellipse
phi = np.linspace(-np.pi/2, np.pi/2, 100)
theta_3d = np.linspace(0, 2 * np.pi, 100)
theta_3d, phi_3d = np.meshgrid(theta_3d, phi)
x_3d = a * np.sign(np.cos(theta_3d)) * np.power(np.abs(np.cos(theta_3d)), 2/n) * np.cos(phi_3d)
y_3d = b * np.sign(np.sin(theta_3d)) * np.power(np.abs(np.sin(theta_3d)), 2/n) * np.cos(phi_3d)
z_3d = np.power(np.abs(np.sin(phi_3d)), 2/n)

# Create a figure with subplots for 2D and 3D
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Plot the Superellipse in 2D
axes[0].plot(x, y)
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].set_title('Superellipse (2D)')

# Plot the Superellipse in 3D
axes[1] = fig.add_subplot(122, projection='3d')
axes[1].plot_surface(x_3d, y_3d, z_3d, cmap='viridis')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')
axes[1].set_zlabel('Z')
axes[1].set_title('Superellipse (3D)')

plt.tight_layout()
plt.show()