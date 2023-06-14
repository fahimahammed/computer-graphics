import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 50)

theta, phi = np.meshgrid(theta, phi)

a = 5
b = 2
c = 4
center = (0,0,0)

x = center[0] + a * np.sin(phi) * np.cos(theta)
y = center[1] + b * np.sin(phi) * np.sin(theta)
z = center[2] + c * np.cos(phi) 

plt.subplot(121)
plt.plot(x, y, 'r.')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.grid(True)
plt.title("Ellipsoid 2D")

ax = plt.subplot(122, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_ylabel('Z')
ax.set_title("Ellipsoid 3D")

plt.tight_layout()
plt.show()