import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 50)
theta, phi = np.meshgrid(theta, phi)

radius = 2
center = (0, 2, 4)

x = center[0] + radius * np.sin(phi) * np.cos(theta)
y = center[1] + radius * np.sin(phi) * np.sin(theta)
z = center[2] + radius * np.cos(phi)

plt.subplot(121)
plt.title("Sphere 2D")
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, y, 'b.')
plt.grid(True)
plt.axis('equal')

ax = plt.subplot(122, projection='3d')
ax.set_title("Sphere 3D")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot_surface(x, y, z, cmap='viridis')

plt.tight_layout()
plt.show()