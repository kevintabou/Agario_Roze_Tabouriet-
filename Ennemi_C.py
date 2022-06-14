# Roze Corentin
# 15/12/2021
# Classe Ennemi Agario
# V0.3.1

from pygame.math import Vector2
import core
import pygame
import random
import math
from Creep_C import Creep_C

class Ennemi_C:
    def __init__(self):
        self.L = 1000
        self.H = 600
        self.pos_E = Vector2(random.randint(0, 600), random.randint(0, 400))
        self.couleur_E = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon_E = 10
        self.gravity_x = 1
        self.gravity_y = 1
        self.pos_E = Vector2(self.pos_E.x + self.gravity_x, self.pos_E.y + self.gravity_y)

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_E, self.pos_E, self.rayon_E)

    def move(self):
        self.pos_E = Vector2(self.pos_E.x + self.gravity_x, self.pos_E.y + self.gravity_y)



         # Hors limite X
        if self.pos_E.x > core.WINDOW_SIZE[0] - self.rayon_E:
                self.gravity_x = -5
                self.vitesse = self.vitesse - self.vitesse
                self.couleur_E = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.pos_E.x < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayon_E:
                self.gravity_x = 5
                self.vitesse = self.vitesse - self.vitesse
                self.couleur_E = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            # Hors limite Y
        if self.pos_E.y > core.WINDOW_SIZE[1] - self.rayon_E:
                self.gravity_y = -5
                self.vitesse = self.vitesse - self.vitesse
                self.couleur_E, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.pos_E.y < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayon_E:
                self.gravity_y = 5
                self.vitesse = self.vitesse - self.vitesse
                self.couleur_E = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def manger(self, listeCreep):
        for c in listeCreep:
            if c.pos_C.distance_to(self.pos_E) < 150:
                self.PS = pygame.Vector2(0, 0)
                self.k = 0.01
                self.l0 = 1
                self.u = 10
                self.vitesse = Vector2(0, 0)

                # Vecteur pos_souris - pos_cercle
                self.PS = pygame.Vector2(c.pos_C.x - self.pos_E.x, c.pos_C.y - self.pos_E.y)

                # Norme vecteur PS
                self.l = self.PS.length()

                # Longueur vecteur PS
                self.u = self.PS.normalize()

                # Calcul Force finale
                self.Fr = self.k * abs(self.l - self.l0) * self.u

                # Vitesse = vitesse + force
                self.vitesse = (self.vitesse + self.Fr)*5

                # pos_cercle = pos_cercle + vitesse
                self.pos_E = self.pos_E + self.vitesse


    def grossir(self):
        self.rayon_E = self.rayon_E + 1