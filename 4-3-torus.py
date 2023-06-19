import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

majorRadius = 2
minorRadius = 1
x = (majorRadius + minorRadius * np.cos(theta)) * np.cos(phi)
y = (majorRadius + minorRadius * np.cos(theta)) * np.sin(phi)
z = minorRadius * np.sin(theta)

plt.subplot(121)
plt.title("Torus 2D")
plt.plot(x, y, 'r.')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')

ax = plt.subplot(122, projection='3d')
ax.set_title("Torus 3D")
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.tight_layout()
plt.show()