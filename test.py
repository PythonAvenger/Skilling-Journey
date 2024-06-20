import logging
import sys

import pygame

def main():
    pygame.init()
    pygame.font.init()

    info = logging.Logger("INFO")
    clock = pygame.Clock()
    text_font = pygame.Font("./assets/fonts/font1.ttf", 20)

    window = pygame.display.set_mode((500, 500))
    surface = pygame.image.load("./assets/images/buttons/button.png").convert_alpha()
    surface = pygame.transform.scale_by(surface, 5)
    text = text_font.render("Start Settings Quit", True, "white", "black", 160)
    text.set_colorkey("black")

    info.info("Text created and blitted onto surface")

    surface.blit(text, (surface.get_rect().centerx - text.get_width()/2, surface.get_rect().centery - text.get_height()/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        window.blit(text, (0, 250))
        pygame.display.update()
        clock.tick(60)
    
