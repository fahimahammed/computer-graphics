import pygame
import sys

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Hidden Surface Elimination")

# Define the shapes with their respective depths and colors
shapes = [
    (pygame.Rect(100, 100, 200, 200), 0, RED),    # Shape 1 with depth 0 and color RED
    (pygame.Rect(150, 150, 200, 200), 1, GREEN),  # Shape 2 with depth 1 and color GREEN
    (pygame.Rect(200, 200, 200, 200), 2, BLUE)    # Shape 3 with depth 2 and color BLUE
]

# Sort the shapes based on depth (Z-order)
sorted_shapes = sorted(shapes, key=lambda shape: shape[1])

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the display
    display.fill(BLACK)

    # Draw the shapes in the sorted order
    for shape, _, color in sorted_shapes:
        pygame.draw.rect(display, color, shape)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit the program
pygame.quit()
sys.exit()
