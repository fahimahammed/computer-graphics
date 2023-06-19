import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate theta values from 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 100)

# Generate phi values from 0 to pi
phi = np.linspace(0, np.pi, 50)

# Create a grid of theta and phi values
theta, phi = np.meshgrid(theta, phi)

# Define the parameters of the ellipsoid
a = 5  # radius along x-axis
b = 2  # radius along y-axis
c = 4  # radius along z-axis
center = (0, 0, 0)  # center of the ellipsoid

# Calculate the coordinates of the points on the ellipsoid
x = center[0] + a * np.sin(phi) * np.cos(theta)
y = center[1] + b * np.sin(phi) * np.sin(theta)
z = center[2] + c * np.cos(phi)

# Plotting the ellipsoid in 2D
plt.subplot(121)
plt.plot(x, y, 'r.')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.grid(True)
plt.title("Ellipsoid 2D")

# Plotting the ellipsoid in 3D
ax = plt.subplot(122, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Ellipsoid 3D")

plt.tight_layout()
plt.show()