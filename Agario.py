# Roze Corentin
# 15/12/2021
# main Agario
# V0.3.1

from pygame.math import Vector2
import core
import pygame
import random
from Creep_C import Creep_C
from Ennemi_C import Ennemi_C
from Joueur_C import Joueur_C

def setup():
    print("Setup START---------")

    core.memory("L", 1000)
    core.memory("H", 600)

    core.fps = 30
    core.WINDOW_SIZE = [core.memory("L"), core.memory("H")]

    core.memory("creep", [])
    core.memory("Joueur",Joueur_C())
    core.memory("Ennemi", [])

    for i in range(100):
        core.memory("creep").append(Creep_C())

    for i in range(5):
        core.memory("Ennemi").append(Ennemi_C())

    print("Setup END-----------")


def run():
    core.cleanScreen()

    for Creep in core.memory("creep"):
        Creep.draw(core.screen)

    for Ennemi in core.memory("Ennemi"):
        Ennemi.draw(core.screen)
        Ennemi.move()

    core.memory("Joueur").draw()
    core.memory("Joueur").move()

    # Joueur mange Creep
    for c in core.memory("creep"):
        if c.pos_C.distance_to(core.memory("Joueur").centredecercle) < core.memory("Joueur").rayonducercle + c.rayon_C:
            core.memory("Joueur").grossir()
            c.mourir()

        for e in core.memory("Ennemi"):
            if c.pos_C.distance_to(e.pos_E) < e.rayon_E + c.rayon_C:
                e.manger(core.memory("creep"))
                e.grossir()
                c.mourir()


    print("RUN")

core.main(setup, run)
