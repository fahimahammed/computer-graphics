import numpy as np
import matplotlib.pyplot as plt

points = np.array([[4, 4], [6, 4], [6, 6], [4, 6], [4, 4]])

# plotting the original squares
plt.figure(figsize=(8, 4))

#plt.subplot(121)
plt.plot(points[:, 0], points[:, 1], 'go-')
plt.title("Original Square")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable = 'box')

# translated points
tPoints = points + np.array([2, 3])
#plt.subplot(122)
plt.plot(tPoints[:, 0], tPoints[:, 1], 'ro-')
plt.title("Translated Square")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable = 'box')

plt.tight_layout()
plt.show()