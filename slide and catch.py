#(lab) slide and catch
#Zechariah Prieshoff
#June 4th, 2024
#A simple, space themed slide and catch game.

import pygame
import simpleGE
import random

class Fuel(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("fuel.png")
        self.setSize(30, 30)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screen.get_width())
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.bottom > self.screen.get_height():
            self.reset()
class Ship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("spaceship.png")
        self.setSize(50, 40)
        self.position = (320, 400)
        self.movespeed = 7

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.movespeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.movespeed
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("arcadespace.jpg")
        self.soundFuel = simpleGE.Sound("powerup.wav")
        self.numFuels = 4
        self.ship = Ship(self)
        self.fuels = []
        for i in range(self.numFuels):
            self.fuels.append(Fuel(self))
        self.sprites = [self.ship, self.fuels]

    def process(self):
        for fuel in self.fuels:
            if fuel.collidesWith(self.ship):
                fuel.reset()
                self.soundFuel.play()



def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()