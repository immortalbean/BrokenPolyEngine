import pygame

# Generic base-class for all game objects

class gameobject():
    def __init__(self, initial_position: pygame.math.Vector2):
        self.position = initial_position