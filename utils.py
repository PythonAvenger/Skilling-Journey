import pygame
pygame.font.init()

class Logo(pygame.sprite.Sprite):
    def __init__(self, centerX, centerY, scale):
        super().__init__()
        self.centerX = centerX
        self.centerY = centerY

        self.original_image = pygame.transform.scale_by(pygame.image.load("assets/images/logo.png").convert_alpha(), scale)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(centerX, centerY))

        self.angle = 0
        self.angle_increment = 0.12
        self.angle_limit = 5

        self.height_limit = 75
        self.height_increase = 0
        self.height_increment = 1

        self.moving_up = True

    def rotate(self):
        self.angle += self.angle_increment
        if self.angle >= self.angle_limit or self.angle <= -self.angle_limit:
            self.angle_increment *= -1

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(self.centerX, self.centerY))

    def animate_up(self):
        if self.height_increment:
            self.height_increase += self.height_increment

        if self.rect.centery == self.height_limit:
            self.height_increment = 0
            self.moving_up = False

        if self.height_increase == 1:
            self.rect.centery -= int(self.height_increase)
            self.centerY -= int(self.height_increase)
            self.height_increase = 0


    def update(self):
        self.rotate()
        if self.moving_up:
            self.animate_up()

class Background(pygame.sprite.Sprite):
    def __init__(self, image, centerx, centery, scale=1):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load(image).convert_alpha(), scale)
        self.rect = self.image.get_rect(center=(centerx, centery))


class Button(pygame.sprite.Sprite):
    ## Img 0 in list is default image, 1 is hovered

    def __init__(self, centerX, centerY, scale, text, img_list: list, function=None):
        super().__init__()
        self.centerX = centerX
        self.centerY = centerY
        self.scale = scale

        # TBD: Want to make individual functions for each button, but the whole game object has to be passed in as a parameter
        self.function = function
        self.clicked = False

        self.images = [pygame.transform.scale_by(pygame.image.load(image).convert_alpha(), self.scale) for image in img_list]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(self.centerX, self.centerY))

        self.font = pygame.font.Font("./assets/fonts/home_screen.otf")
        self.label = self.font.render(text, True, "black", "white", 160)
        self.label.set_colorkey("white")

        for image in self.images:
            image.blit(self.label, (image.get_width()//1.4 - self.label.get_width()/2, image.get_height()/2 - self.label.get_height()/2))

        self.hovered = False

    def button_hovered(self):
        if self.hovered:
            self.image = self.images[1]
        else:
            self.image = self.images[0]

    def update(self):
        self.button_hovered()


class Save_Data():
    def __init__(self, json):
        self.json = json
        

def path_wrapper(path: str, files: list):
    return [f"{path}{img}" for img in files]

def pixel_perfect_collision(object: pygame.sprite.GroupSingle):
    mouse_pos = pygame.mouse.get_pos()
    mouse_mask = pygame.mask.from_surface(pygame.Surface((1, 1), pygame.SRCALPHA))  # Create a mask for the mouse cursor
    mouse_mask.set_at((0, 0), 1)  # Set a single pixel in the mask

    surface_mask = pygame.mask.from_surface(object.sprite.image)

    return surface_mask.overlap(mouse_mask, (mouse_pos[0] - object.sprite.rect.left, mouse_pos[1] - object.sprite.rect.top))
