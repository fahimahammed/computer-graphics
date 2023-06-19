import matplotlib.pyplot as plt
import numpy as np

def computeBezierCurve(controlPoints, numPoints):
    t = np.linspace(0, 1, numPoints)
    n = len(controlPoints) - 1
    curvePoints = np.zeros((numPoints, 2))

    for i in range(numPoints):
        for j in range(n + 1):
            curvePoints[i] += controlPoints[j] * binomialCoefficient(n, j) * (1 - t[i]) ** (n - j) * t[i] ** j

    return curvePoints

def binomialCoefficient(n, k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))

# Define control points
controlPoints = np.array([[0, 0], [2, 5], [5, 3], [10, 8]])

# Compute Bezier curve points
numPoints = 100
curvePoints = computeBezierCurve(controlPoints, numPoints)

# Plot the Bezier curve
plt.plot(controlPoints[:, 0], controlPoints[:, 1], 'ro-', label='Control Points')
plt.plot(curvePoints[:, 0], curvePoints[:, 1], 'b-', label='Bezier Curve')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bezier Curve')
plt.grid(True)
plt.show()
