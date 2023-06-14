import matplotlib.pyplot as plt

def draw_line(x0, y0, x1, y1):
    # Calculate the differences and absolute values
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Determine the slope of the line
    is_steep = dy > dx

    # Swap the coordinates if the line is steep
    if is_steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    # Swap the endpoints if x0 > x1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    # Recalculate the differences and absolute values
    dx = x1 - x0
    dy = abs(y1 - y0)

    # Calculate the decision parameter
    p = 2 * dy - dx

    # Determine the direction of increment in y
    y_step = 1 if y0 < y1 else -1

    # Generate the points of the line
    x = x0
    y = y0
    points = []
    for _ in range(dx + 1):
        # Append the current point to the list
        point = (y, x) if is_steep else (x, y)
        points.append(point)

        # Update the decision parameter
        p += 2 * dy
        if p >= 0:
            y += y_step
            p -= 2 * dx

        # Move to the next x-coordinate
        x += 1

    return points

# Define the line coordinates
x0, y0 = 1, 1
x1, y1 = 8, 5

# Call the line drawing function
line_points = draw_line(x0, y0, x1, y1)

# Print the points
print("Line Points:")
for point in line_points:
    print(point)

# Plot the line
x_coords, y_coords = zip(*line_points)
plt.plot(x_coords, y_coords, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bresenham Line Drawing')
plt.grid(True)
plt.show()
