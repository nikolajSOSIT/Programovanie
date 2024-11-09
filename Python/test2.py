import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Example")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Set up font
font = pygame.font.Font(None, 74)
text = font.render("Hello, Pygame!", True, white)

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    window.fill(blue)
    
    # Draw text
    window.blit(text, (150, 250))
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
