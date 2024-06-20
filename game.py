import pygame
import sys
from utils import *

class Game():
    def __init__(self, tick_speed):
        pygame.init()

        self.WIDTH = 1024
        self.HEIGHT = 768
        self.button_path = "assets/images/buttons/"
        self.TICK_SPEED = tick_speed

        self.bg_color = (0, 0, 0)

        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        self.clock = pygame.Clock()

        self.screens = ["home", "main", "settings", "guide"]
        self.screen = self.screens[0]

        self.overlays = ["upgrades", "achievements", "husbandry"]
        self.overlay = self.overlays[0]
        
        self.home_screen_init()

        
    def home_screen_init(self):
        self.logo = pygame.sprite.GroupSingle(Logo(self.WIDTH/2, self.HEIGHT/2, 2.2))
        self.start_button = pygame.sprite.GroupSingle(Button(125, 200, 1, "Start", path_wrapper(self.button_path, ["button.png", "button_darkened.png"])))
        self.saves_button = pygame.sprite.GroupSingle(Button(125, 275, 1, "Saves", path_wrapper(self.button_path, ["button.png", "button_darkened.png"])))
        self.settings_button = pygame.sprite.GroupSingle(Button(125, 350, 1, "Settings", path_wrapper(self.button_path, ["button.png", "button_darkened.png"])))
        self.quit_button = pygame.sprite.GroupSingle(Button(125, 425, 1, "Quit", path_wrapper(self.button_path, ["button.png", "button_darkened.png"])))
        self.background = pygame.sprite.GroupSingle(Background("assets/images/backgrounds/bg3.png", self.WIDTH/2, self.HEIGHT/2))
        self.home_buttons = [self.start_button, self.saves_button, self.settings_button, self.quit_button]

    def render(self, screen, render_order=None):
        if screen == "home":
            self.window.fill(self.bg_color)
            for component in render_order:
                component.draw(self.window)

            for component in render_order:
                component.update()

        elif screen == "main":
            self.window.fill(self.bg_color)

    def run(self):
        running = True
        while running:

            #Event checking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # When left click button is clicked
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.screen == "home" and self.logo.sprite.moving_up == False:
                        if pixel_perfect_collision(self.start_button):
                            self.start_button.sprite.clicked = True
                            self.screen = "main"
                        elif pixel_perfect_collision(self.quit_button):
                            pygame.quit()
                            sys.exit()
                        

            # Rendering screen components
            if self.logo.sprite.moving_up:
                self.render(self.screen, [self.background, self.logo])
            else: self.render(self.screen, [self.background, self.logo, self.start_button, self.saves_button, self.settings_button, self.quit_button])

            if self.screen == "home" and self.logo.sprite.moving_up == False:
                for button in self.home_buttons:
                    if pixel_perfect_collision(button):
                        button.sprite.hovered = True
                    else: button.sprite.hovered = False 

            elif self.screen == "main":
                self.render(self.screen)

            pygame.display.update()

            self.clock.tick(self.TICK_SPEED)