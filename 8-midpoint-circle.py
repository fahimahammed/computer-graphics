import matplotlib.pyplot as plt

def plot_points(x, y, xc, yc):
    """
    Plot the points of the circle using symmetry.
    """
    plt.plot(xc + x, yc + y, 'ro')
    plt.plot(xc - x, yc + y, 'ro')
    plt.plot(xc + x, yc - y, 'ro')
    plt.plot(xc - x, yc - y, 'ro')
    plt.plot(xc + y, yc + x, 'ro')
    plt.plot(xc - y, yc + x, 'ro')
    plt.plot(xc + y, yc - x, 'ro')
    plt.plot(xc - y, yc - x, 'ro')

def midpoint_circle(xc, yc, r):
    """
    Draw a circle using the Midpoint Circle Drawing Algorithm.
    """
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter

    # Plot the first point
    plot_points(x, y, xc, yc)

    while x < y:
        x += 1

        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        # Plot the points
        plot_points(x, y, xc, yc)

    plt.axis('equal')
    plt.show()

# Example usage
x_center = 0
y_center = 0
radius = 5

midpoint_circle(x_center, y_center, radius)

# center (xc, yc)
# x0 = 0; y0 = r
# Decision parameter, P = 1 - r
# if P < 0 then, x = x+1; y = y; p = p + 2x + 1
# else x = x + 1; y = y-1; p = p-2(x-y)+1