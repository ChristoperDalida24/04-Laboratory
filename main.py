import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up display
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("04 Lab 1 - Christoper John R. Dalida")

# Enable depth test
glEnable(GL_DEPTH_TEST)

# Set up perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)

# Define vertices of a cube
vertices = [
    (1, 1, 1),    # 0
    (1, 1, -1),   # 1
    (1, -1, -1),  # 2
    (1, -1, 1),   # 3
    (-1, 1, 1),   # 4
    (-1, -1, -1), # 5
    (-1, -1, 1),  # 6
    (-1, 1, -1),  # 7
]

# Define triangles (each triangle has 3 vertices)
triangles = [
    (0, 1, 2), (0, 2, 3),  # Front face
    (4, 7, 6), (7, 5, 6),  # Back face
    (0, 4, 3), (4, 6, 3),  # Left face
    (1, 5, 2), (1, 7, 5),  # Right face
    (0, 1, 7), (0, 7, 4),  # Top face
    (3, 2, 5), (3, 5, 6)   # Bottom face
]

# Define colors for each pair of triangles
colors = [
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 1, 0),  # Yellow
    (1, 0, 1),  # Magenta
    (0, 1, 1)   # Cyan
]

# Function to draw the cube using triangles
def draw_cube():
    glBegin(GL_TRIANGLES)
    for i, triangle in enumerate(triangles):
        glColor3fv(colors[i // 2])  # Set a specific color for each pair of triangles
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Apply keyboard controls for translation
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Move left
                glTranslatef(-1, 0, 0)
            if event.key == pygame.K_d:  # Move right
                glTranslatef(1, 0, 0)
            if event.key == pygame.K_w:  # Move up
                glTranslatef(0, 1, 0)
            if event.key == pygame.K_s:  # Move down
                glTranslatef(0, -1, 0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glRotatef(1, 1, 1, 1)  # Rotate the cube

    draw_cube()

    pygame.display.flip()
    pygame.time.wait(15)