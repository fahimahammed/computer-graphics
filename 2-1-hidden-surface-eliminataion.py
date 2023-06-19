import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D grid
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(x, y)

# Define the heights for each point in the grid
Z = X**2 + Y**2  # Adjust this function based on your desired shape

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set the aspect ratio of the plot
ax.set_box_aspect([1, 1, 1])

# Set the axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the plot title
ax.set_title('Hidden Surface Elimination')

# Show the plot
plt.show()
