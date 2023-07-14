import pygame

from funciones_utiles import * 

class Fireball:    
    def __init__(self,path,pos,size,frame) -> None:
        self.surface = getSurface(path=path,frame=frame,flag_flip=False,size=size)
        self.rect = self.surface.get_rect(topleft=pos)
        self.cooldown = 10000
        self.is_avaible = True
        self.is_collition = False
        self.speed = 0

    def update(self,world_move):
        self.rect.x += world_move.x + self.speed
        
        if not self.is_avaible:
            current_time = pygame.time.get_ticks()
            if (current_time - self.last_fireball) >= self.cooldown:
                self.is_avaible = True

    def draw(self,screen):
        screen.blit(self.surface,self.rect)