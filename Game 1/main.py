import pygame
from math import ceil
import webbrowser
#import time
import InputManager
#displayX = int(input("Pixel x"))
#displayY = int(input("Pixel y"))
displayX = 500
displayY = 500
refreshrate = 30
walkSpeed = 3

class player():
     def __init__(self) -> None:
          self.x = displayX / 2
          self.y = displayY / 2
          pass
     
i = 1,1,1

print(i)


background = pygame.image.load("Sprites/background.png")
playerIdle_raw = pygame.image.load("Sprites/playerIdle.png")
playerIdle = pygame.transform.scale(playerIdle_raw,(100,100))

print("start---------------------------------------------")
Bsize = {"x" : background.get_width(),
         "y" : background.get_height() 
        }

print(Bsize)

def Tile(size, bSize):
    amount = size / bSize
    return amount

amountX = ceil(Tile(displayX,Bsize["x"]))
amountY = ceil(Tile(displayX,Bsize["x"]))



display = pygame.display.set_mode ([displayX, displayY])
clock = pygame.time.Clock()
print(f"Dein Game wird {displayX} p * {displayY} p groß sein.")



def bgDraw():
    #Background Stuff... DONT TOUCH https://i.redd.it/6ei98jxs2kk81.jpg
        bgX = 0
        bgY = 0


        for o in range(0,amountY):

            for i in range(0,amountX):
                #print(bgX)
                display.blit(background,(i*Bsize["x"],o * Bsize["y"]))
                bgX + Bsize["x"]
                
            #print(bgY)
            bgY + Bsize["y"]


player1 = player()
oiaszugetoezeeieeeeegeteeoe = True
while True:

    
    Inputs = InputManager.InpuManager()
    print(Inputs)
    
    display.fill((0,0,0))

    
    #Inputs = InputManager.InpuManager()
                 
            


   
    player1.y = player1.y + Inputs["vertical"] * walkSpeed * -1
    player1.x = player1.x + Inputs["horizontal"] * walkSpeed
    

    
    bgDraw()


    
    

    
    display.blit(playerIdle,(player1.x, player1.y))


    
    
















    pygame.display.flip()
    pygame.display.update()
    clock.tick(refreshrate)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
       
    







