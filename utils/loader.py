import pygame


## load images
def load_image(filename, size=None):
    path = f"assets/images/{filename}"
    image = pygame.image.load(path)
    if size:
        image = pygame.transform.scale(image, size)
    return image
