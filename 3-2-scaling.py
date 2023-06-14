import numpy as np
import matplotlib.pyplot as plt

points = np.array([[-1, -1],
                   [1, -1],
                   [1, 1],
                   [-1, 1],
                   [-1, -1]])

plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.plot(points[:, 0], points[:, 1], 'ro-')
plt.title("Original square")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')

sPoints = points * np.array([2, 3])
plt.subplot(122)
plt.plot(sPoints[:, 0], sPoints[:, 1], 'go-')
plt.title("Scaled square")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.show()
