from Sky import Sky
from ship import Ship
import random
import pygame

class Game:
    
    def __init__(self):
        self.ship=Ship() 
        self.width=900 
        self.height=900 
        self.mySky=Sky(self.width, self.height, 1600) 
        self.screen=pygame.display.set_mode((self.width,self.height)) 
        self.clock=pygame.time.Clock()
        self.fps=60 
        self.sprites= pygame.image.load("sprites.png") 
        self.shipsprite=pygame.Surface((64,64)).convert() 
        self.shipsprite.blit(self.sprites,(0,0),(250,436,64,64)) 
        
    def checkKeys(self):
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.ship.direction="RIGHT" 
        elif keys[pygame.K_LEFT]: self.ship.direction="LEFT"
        else: self.ship.direction="STOP"
        
        if self.ship.xnave > self.width-65: self.ship.xnave=self.width-65 
        if self.ship.xnave < 5: self.ship.xnave=5 
        

    def run (self):
        pygame.init()
        
        control=True
        while control:
            self.screen.fill((0,0,0))
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()

            for star in self.mySky.stars:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                pygame.draw.circle(self.screen, (r,g,b), star, 1)
            
            self.mySky.move() 
            self.ship.move() 
            x=self.ship.xnave 
            y=self.ship.ynave 
            self.screen.blit(self.shipsprite, (x,y)) 
            self.clock.tick(self.fps) 
            self.checkKeys() 
            pygame.display.flip() 


myGame=Game() 
myGame.run() 