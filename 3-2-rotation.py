import numpy as np
import matplotlib.pyplot as plt
import math

# points = np.array([[4, 4], [6, 4], [6, 6], [4, 6], [4, 4]])
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

#red angle
rad_angle = math.radians(45)
# rotation matrix
rotation_matrix = np.array([[math.cos(rad_angle), -math.sin(rad_angle)], [math.sin(rad_angle), math.cos(rad_angle)]])
rPoints = np.dot( points, rotation_matrix)

plt.subplot(122)
plt.plot(rPoints[:, 0], rPoints[:, 1], 'go-')
plt.title("Rotated square")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
#plt.gca().set_aspect('equal', adjustable = 'box')

plt.tight_layout()
plt.show()

print("original points: ", points)