from src import controller
import pygame

def main():
    pygame.init()

    main_window = controller.Controller()
    main_window.mainLoop()

main()
