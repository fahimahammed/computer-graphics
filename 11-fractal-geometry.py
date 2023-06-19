import turtle

def drawSierpinski(length, depth):
    if depth == 0:
        # Base case: draw a single triangle
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        # Recursive case: draw three smaller triangles
        drawSierpinski(length / 2, depth - 1)
        turtle.forward(length / 2)
        drawSierpinski(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        drawSierpinski(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

# Set up the turtle graphics window
turtle.speed(1)  # Fastest speed
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

# Call the function to draw the Sierpinski triangle
drawSierpinski(500, 5)

# Keep the window open until it is manually closed
turtle.done()
