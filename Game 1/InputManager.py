import pygame
PlayerInput = { "vertical" : 0,
                "horizontal" : 0,
                  
                  }

def InpuManager():
        
    

    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: #Input wird True

                if event.key == pygame.K_a:
                    PlayerInput["horizontal"] = -1          

                if event.key == pygame.K_d:
                    PlayerInput["horizontal"] = 1

                if event.key == pygame.K_w:
                    PlayerInput["vertical"] = 1

                if event.key == pygame.K_s:
                    PlayerInput["vertical"] = -1

            if event.type == pygame.KEYUP: #Input wird False

                if event.key == pygame.K_a:
                      PlayerInput["horizontal"] = 0
                
                if event.key == pygame.K_d:
                     PlayerInput["horizontal"] = 0
                 
                if event.key == pygame.K_s:
                     PlayerInput["vertical"] = 0
                
                if event.key == pygame.K_w:
                     PlayerInput["vertical"] = 0



    
    
    return PlayerInput