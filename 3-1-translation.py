import numpy as np
import matplotlib.pyplot as plt

# Define the points of the original square
#points = np.array([[4, 4], [6, 4], [6, 6], [4, 6], [4, 4]])
points = np.array([[4, 4], [6, 4], [4, 6], [4, 4]])

# Plotting the original square
plt.figure(figsize=(8, 4))

plt.subplot(121)
plt.plot(points[:, 0], points[:, 1], 'go-')  # Plot the points of the original square
plt.title("Original Square")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')  # Set equal aspect ratio for x and y axes

# Translate the points
translated_points = points + np.array([2, 3])

plt.subplot(122)
plt.plot(translated_points[:, 0], translated_points[:, 1], 'ro-')  # Plot the translated points
plt.title("Translated Square")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')  # Set equal aspect ratio for x and y axes

plt.tight_layout()
plt.show()