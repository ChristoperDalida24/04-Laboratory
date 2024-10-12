import pygame

from pygame.locals import *

from OpenGL.GL import *

from OpenGL.GLU import *

 

# Initialize Pygame

pygame.init()

 

# Set up display

display = (800, 600)

pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

pygame.display.set_caption("3D Diamond Example")

 

# Enable depth test

glEnable(GL_DEPTH_TEST)

 

# Set up perspective

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glTranslatef(0, 0, -5)

 

# Define vertices of a diamond shape

vertices = [

    (0, 1, 0), # Top

    (-1, 0, -1), # Bottom left front

    (1, 0, -1), # Bottom right front

    (1, 0, 1), # Bottom right back

    (-1, 0, 1), # Bottom left back

    (0, -1, 0), # Bottom

]

 

# Define triangles

triangles = [

    (0, 1, 2), # Top triangle front

    (0, 2, 3), # Top triangle right

    (0, 3, 4), # Top triangle back

    (0, 4, 1), # Top triangle left

    (5, 1, 2), # Bottom triangle front

    (5, 2, 3), # Bottom triangle right

    (5, 3, 4), # Bottom triangle back

    (5, 4, 1), # Bottom triangle left

]

 

# Define colors for each triangle

colors = [

    (1, 0, 0), # Red

    (0, 1, 0), # Green

    (0, 0, 1), # Blue

    (1, 1, 0), # Yellow

    (1, 0, 1), # Magenta

    (0, 1, 1), # Cyan

]

 

# Function to draw the diamond

def draw_diamond():

    glBegin(GL_TRIANGLES)

    for i, triangle in enumerate(triangles):

        glColor3fv(colors[i % len(colors)]) # Set color

        for vertex in triangle:

            glVertex3fv(vertices[vertex])

    glEnd()

 

# Main loop

scale_factor = 1.0 # Initialize scale factor

rotation_speed = 0.5 # Default rotation speed

rotation_axis = (1, 1, 1) # Default rotation axis

 

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            quit()

 

        # Apply keyboard controls for translation and scaling

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a: # Move left

                glTranslatef(-0.1, 0, 0)

            if event.key == pygame.K_d: # Move right

                glTranslatef(0.1, 0, 0)

            if event.key == pygame.K_w: # Move up

                glTranslatef(0, 0.1, 0)

            if event.key == pygame.K_s: # Move down

                glTranslatef(0, -0.1, 0)

            if event.key == pygame.K_q: # Scale down

                scale_factor = max(scale_factor - 0.1, 0.1)

                glScalef(0.9, 0.9, 0.9)

            if event.key == pygame.K_e: # Scale up

                scale_factor += 0.1

                glScalef(1.1, 1.1, 1.1)

            if event.key == pygame.K_UP: # Increase rotation speed

                rotation_speed += 0.1

            if event.key == pygame.K_DOWN: # Decrease rotation speed

                rotation_speed = max(0.1, rotation_speed - 0.1)

            if event.key == pygame.K_LEFT: # Rotate around Y axis

                rotation_axis = (0, 1, 0)

            if event.key == pygame.K_RIGHT: # Rotate around X axis

                rotation_axis = (1, 0, 0)

 

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

 

    # Rotate the diamond clockwise

    glRotatef(-rotation_speed, *rotation_axis) # Use negative rotation for clockwise

 

    draw_diamond()

 

    pygame.display.flip()

    pygame.time.wait(5)