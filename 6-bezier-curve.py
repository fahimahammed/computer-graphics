#Problem 6
import matplotlib.pyplot as plt
import numpy as np

def compute_bezier_curve(control_points, num_points):
    t = np.linspace(0, 1, num_points)
    n = len(control_points) - 1
    curve_points = np.zeros((num_points, 2))

    for i in range(num_points):
        for j in range(n + 1):
            curve_points[i] += control_points[j] * binomial_coefficient(n, j) * (1 - t[i]) ** (n - j) * t[i] ** j

    return curve_points

def binomial_coefficient(n, k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))

# Define control points
control_points = np.array([[0, 0], [2, 5], [5, 3], [7, 8]])

# Compute Bezier curve points
num_points = 100
curve_points = compute_bezier_curve(control_points, num_points)

# Plot the Bezier curve
plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Bezier Curve')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bezier Curve')
plt.grid(True)
plt.show()