import os
import pygame


# Helper function to load an image file
def load_image(file_path):
    full_path = os.path.join("assets", file_path)
    return pygame.image.load(full_path).convert_alpha()
