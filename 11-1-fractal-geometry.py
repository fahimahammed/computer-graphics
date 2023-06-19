import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def create_fractal(width, height, zoom, x_offset, y_offset, max_iter):
    pixels = np.empty((width, height))
    for x in range(width):
        for y in range(height):
            real = (x - width/2 + x_offset) / (zoom * width/2)
            imag = (y - height/2 + y_offset) / (zoom * height/2)
            c = complex(real, imag)
            pixels[x, y] = mandelbrot(c, max_iter)
    return pixels

# Set the size and properties of the fractal image
width = 800
height = 800
zoom = 1.0
x_offset = 0.0
y_offset = 0.0
max_iter = 256

# Generate the fractal image
fractal = create_fractal(width, height, zoom, x_offset, y_offset, max_iter)

# Plot the fractal using matplotlib
plt.imshow(fractal.T, cmap='hot', origin='lower')
plt.title('Mandelbrot Set')
plt.axis('off')
plt.show()
