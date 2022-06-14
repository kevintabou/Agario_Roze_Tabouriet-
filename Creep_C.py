# Roze Corentin
# 15/12/2021
# Classe Creep Agario
# V0.3.1

from pygame.math import Vector2
import core
import pygame
import random
import math


class Creep_C:
    def __init__(self):

        self.L = 1000
        self.H = 600
        self.pos_C = Vector2(random.randint(0, self.L), random.randint(0, self.H))
        self.couleur_C = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon_C = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_C, self.pos_C, self.rayon_C)

    def mourir(self):
        self.pos_C = Vector2(random.randint(0, self.L), random.randint(0, self.H))