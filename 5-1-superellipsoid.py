import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up the parameters
a = 100  # x-axis radius
b = 100  # y-axis radius
c = 100  # z-axis radius
n1 = 2   # exponent for x-axis
n2 = 2   # exponent for y-axis
n3 = 2   # exponent for z-axis

# Set up the transformation variables
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)

# Calculate the vertices of the superellipsoid
x = np.outer(np.cos(theta), np.sin(phi))
y = np.outer(np.sin(theta), np.sin(phi))
z = np.outer(np.ones(np.size(theta)), np.cos(phi))
x = a * np.sign(x) * np.power(np.abs(x), n1)
y = b * np.sign(y) * np.power(np.abs(y), n2)
z = c * np.sign(z) * np.power(np.abs(z), n3)

# Plot the Superellipsoid in 2D and 3D side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot the Superellipsoid in 2D
axes[0].contourf(x, y, levels=100)
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].set_title('Superellipsoid (2D)')

# Plot the Superellipsoid in 3D
axes[1] = fig.add_subplot(122, projection='3d')
axes[1].plot_surface(x, y, z, cmap='cool')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')
axes[1].set_zlabel('Z')
axes[1].set_title('Superellipsoid (3D)')

plt.tight_layout()
plt.show()