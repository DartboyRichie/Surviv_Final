import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))

#color of the background/ setting 
green = (107,142,35)
screen.fill(green)

class Obstacles(pygame.sprite.Sprite):

    def __init__(self, obstype, Pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(obstype+".gif")  #.gif being in string format
        self.rect = self.image.get_rect()  
        self.rect.topleft = Pos
        
def move(self, pixels):
    self.rect.x += pixels

#Creating the sprite group for the obstacles in the game 
barrel = Obstacles("barrel", (100,100))
obstacles = pygame.sprite.Group(barrel)

#the bush along with the stone are added to the group initialized by the stone
bush = Obstacles("bush", (200,200))
obstacles.add(bush) #adding the bush to the group

stone = Obstacles("stone", (300, 300))
obstacles.add(stone) 

obstacles.draw(screen)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.KEYPRESSED:
            obstacles.move(Pos(0,-10))
        

##while running:
##    sprites.update()
##    draw(obstype)
        
##def main():
##    #The graphics window is created 
##    win = GraphWin( "Surviv.io for dummies", 1280, 720)
##
##    #Setting the color of the screen, by putting an overlay on top
##    screen = Rectangle( Point(0,0), Point(1280, 720))
##    screen.setFill("olivedrab")
##    screen.draw(win)
##    
##
##    win.getMouse()
##    win.close()
##
##main()
