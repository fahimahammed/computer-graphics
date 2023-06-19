import matplotlib.pyplot as plt

def drawLine(x0, y0, x1, y1):
    # Calculate the differences and absolute values
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Determine the slope of the line
    isSteep = dy > dx

    # Swap the coordinates if the line is steep
    if isSteep:
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
    yStep = 1 if y0 < y1 else -1

    # Generate the points of the line
    x = x0
    y = y0
    points = []
    for _ in range(dx + 1):
        # Append the current point to the list
        point = (y, x) if isSteep else (x, y)
        points.append(point)

        # Update the decision parameter
        p += 2 * dy
        if p >= 0:
            y += yStep
            p -= 2 * dx

        # Move to the next x-coordinate
        x += 1

    return points

# Define the line coordinates
x0, y0 = 1, 5
x1, y1 = 8, 9

# Call the line drawing function
linePoints = drawLine(x0, y0, x1, y1)

# Print the points
print("Line Points:")
for point in linePoints:
    print(point)

# Plot the line
xCoords, yCoords = zip(*linePoints)
plt.plot(xCoords, yCoords, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bresenham Line Drawing')
plt.grid(True)
plt.show()
