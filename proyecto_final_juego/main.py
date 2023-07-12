import pygame
from constantes import *
from gui_main_menu import Main_menu
from mapa import Mapa

pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

pygame.init()

tiempo = pygame.time.Clock()
esta_corriendo = True

def event(event_type):
    print(event_type)

main_menu = Main_menu(name="main_menu",main_screen=pantalla,x=ANCHO_PANTALLA/4,y=0,w=ANCHO_MENU,h=ALTO_MENU,path=PATH_MENU,image_name="0",active=True,setup_menu=SETUP_MAIN_MENU)

mapa_1 = Mapa(level_map,pantalla)

# bucle principal
while esta_corriendo:
    delta_ms = tiempo.tick(FPS)  
    keys = pygame.key.get_pressed() 
    event_list = pygame.event.get()
    for event in event_list: 
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] or main_menu.button_dict["exit"].is_active:
            esta_corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        # menu.update(event=event)

    #Update jugador, enemigo, mapa, etc
    # mapa_1.run(delta_ms)

    if main_menu.is_active:
        main_menu.draw(event_list)

    pygame.display.flip()
    
pygame.quit()   