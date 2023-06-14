import pygame
import sys
from math import sin, cos

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Define the vertices of the 3D object
cube_vertices = [
    (-2, -2, -2),
    (-2, 2, -2),
    (2, 2, -2),
    (2, -2, -2),
    (-2, -2, 2),
    (-2, 2, 2),
    (2, 2, 2),
    (2, -2, 2)
]
# Define the edges of the 3D object
cube_edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Define the faces of the 3D object with colors
cube_faces = [
    ((0, 1, 2, 3), RED),
    ((3, 2, 6, 7), GREEN),
    ((7, 6, 5, 4), BLUE),
    ((4, 5, 1, 0), YELLOW),
    ((5, 6, 2, 1), CYAN),
    ((7, 4, 0, 3), MAGENTA)
]

# Initialize pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Hidden Surface Elimination")

# Define the camera position
camera_pos = (0, 0, -5)

# Define the projection plane
projection_plane_z = 0

# Define the viewing angle
fov = 90

# Define the rotation angles
rotation_angle_x = 0
rotation_angle_y = 0

# Rotate the cube vertices
def rotate(vertices, angle_x, angle_y):
    rotated_vertices = []
    for vertex in vertices:
        x, y, z = vertex

        # Rotate around X-axis
        y_rot = y * cos(angle_x) - z * sin(angle_x)
        z_rot = y * sin(angle_x) + z * cos(angle_x)

        # Rotate around Y-axis
        x_rot = x * cos(angle_y) + z_rot * sin(angle_y)
        z_rot = -x * sin(angle_y) + z_rot * cos(angle_y)

        rotated_vertices.append((x_rot, y_rot, z_rot))
    return rotated_vertices

# Project the 3D vertices onto the 2D projection plane
def project(vertices):
    projected_vertices = []
    for vertex in vertices:
        x, y, z = vertex
        if z == camera_pos[2]:
            z += 0.01  # Avoid division by zero
        distance = camera_pos[2] - z
        factor = fov / distance
        x_proj = int(x * factor + display_width / 2)
        y_proj = int(y * factor + display_height / 2)
        projected_vertices.append((x_proj, y_proj))
    return projected_vertices

# Draw the 3D object on the display
def draw(vertices, edges, faces):
    # Clear the display
    display.fill(BLACK)

    # Project the vertices
    projected_vertices = project(vertices)

    # Draw the faces
    for face, color in faces:
        vertices_list = [projected_vertices[vertex] for vertex in face]
        pygame.draw.polygon(display, color, vertices_list)

    # Draw the edges
    #for edge in edges:
        #vertex1, vertex2 = projected_vertices[edge[0]], projected_vertices[edge[1]]
        #pygame.draw.line(display, WHITE, vertex1, vertex2, 3)

    # Draw the camera marker
    camera_marker_pos = project([camera_pos])[0]
    pygame.draw.circle(display, WHITE, camera_marker_pos, 5)

    # Draw the text "camera" next to the camera marker
    font = pygame.font.SysFont(None, 20)
    text = font.render("Camera", True, WHITE)
    text_rect = text.get_rect()
    text_rect.x = camera_marker_pos[0] + 10
    text_rect.y = camera_marker_pos[1] - 10
    display.blit(text, text_rect)

    # Update the display
    pygame.display.update()

# Create a slider class
class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, initial_val, color, handle_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.color = color
        self.handle_color = handle_color

    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
        handle_x = self.x + int((self.value - self.min_val) / (self.max_val - self.min_val) * self.width)
        pygame.draw.circle(display, self.handle_color, (handle_x, self.y + self.height // 2), self.height // 2)

    def update(self, mouse_x):
        if mouse_x < self.x:
            self.value = self.min_val
        elif mouse_x > self.x + self.width:
            self.value = self.max_val
        else:
            relative_x = mouse_x - self.x
            self.value = self.min_val + (self.max_val - self.min_val) * relative_x / self.width

# Create a slider for X-axis rotation
slider_x = Slider(50, 550, 700, 20, -3.14, 3.14, rotation_angle_x, WHITE, RED)

# Create a slider for Y-axis rotation
slider_y = Slider(50, 580, 700, 20, -3.14, 3.14, rotation_angle_y, WHITE, RED)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            if pygame.mouse.get_pressed()[0]:
                slider_x.update(mouse_x)
                slider_y.update(mouse_x)

    # Rotate the cube
    rotation_angle_x = slider_x.value
    rotation_angle_y = slider_y.value
    cube_vertices_rotated = rotate(cube_vertices, rotation_angle_x, rotation_angle_y)

    # Sort the faces based on their distance from the camera
    sorted_faces = sorted(cube_faces, key=lambda face: max(cube_vertices_rotated[vertex][2] for vertex in face[0]), reverse=True)

    # Draw the cube
    draw(cube_vertices_rotated, cube_edges, sorted_faces)

    # Draw the sliders
    slider_x.draw()
    slider_y.draw()

    # Limit the frame rate
    clock.tick(60)

# Quit the program
pygame.quit()
sys.exit()