'''
Contains components of the game like the Logo, Background, and Button classes, as well as some functionality.
'''

from typing import Union, List, Callable

import pygame
pygame.font.init()

class Logo(pygame.sprite.Sprite):
    '''
    Represents the Logo
    
    Attributes
    ----------
    centerX: int
    centerY: int
    scale: Union[int, float]
    
    
    Methods
    -------
    rotate():
        Rotates the logo for animation purposes
    animate_up():
        Moves the logo up the screen till a certain point
    update():
        Calls all other functions for log update
    '''
    
    def __init__(self, centerX: int, centerY: int, scale: Union[int, float]):
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

class Background(pygame.sprite.Sprite): #TODO: Work on background class
    '''
    Represents the background objects
    
    Attributes
    ----------
    image: str
    centerx: int
    centery: int
    scale: Union[int, float]
    '''
    def __init__(self, image: str, centerx: int, centery: int, scale: Union[int, float]=1):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load(image).convert_alpha(), scale)
        self.rect = self.image.get_rect(center=(centerx, centery))

class Button(pygame.sprite.Sprite):
    '''
    Represents button objects.

    Attributes
    ----------
    centerX : int
    centerY: int
    scale: Union[int, float]
    text: str
    img_list: List[str]
    function: Callable
    
    Methods
    -------
    button_hovered():
        Changes the image of button if mouse hovers over it
    update():
        Calls all button updates
    '''
    
    ## Img 0 in list is default image, 1 is hovered

    def __init__(self, centerX: int, centerY: int, scale: Union[int, float], text: str, img_list: List[str], function: Callable=None): # FIXME: function should not be auto assigned
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
        if self.clicked:
            self.function()
            self.clicked = False

# TODO: Plan save data formatting
class SaveData():
    def __init__(self, json):
        self.json = json

# TODO: Make more friendly to use in code, a but difficult to use. Also make a doctstring
class SpriteSheet():
    def __init__(self, file, rows, columns, width, length):
        self.file = file
        self.sprites = self.get_sprites(rows, columns, width, length)

    def get_sprites(self, rows, columns, width, length):
        spritesheet = pygame.image.load(self.file).convert_alpha()

        x = 0
        y = 0
        sprites = []
        
        for row in range(rows):
            for column in range(columns):
                sprite = pygame.Surface((width, length))
                sprite.blit(spritesheet, (0, 0), pygame.Rect(x, y, x + width, y + length))
                sprites.append(SpriteSheetImage(sprite, row, column, width, length))
                
                print(f"Row: {row}")
                print(f"Column: {column}")
                print(f"({x}, {y})")
                x += width
            y += length
            x = 0

        return sprites
    
class SpriteSheetImage():
    def __init__(self, image: pygame.Surface, row, column, width, length):
        self.image = image
        self.row = row
        self.column = column
        self.width = width
        self.length = length

def path_wrapper(path: str, files: List[str]) -> List[str]:
    '''
    Returns a list of file paths
    
    
    Parameters
    ----------
    path : str
        The path that is concatenated with each file in the files list.
    files : List[str]
        The files to be concatenated to a path.

    Returns
    -------
    List[str]
        A list containing the full paths of each file passed into files param.
    '''
    return [f"{path}{img}" for img in files]

def pixel_perfect_collision(item: pygame.sprite.GroupSingle) -> bool:
    '''
    Determines mouse collision for non rectangular shapes.
    
    Parameters
    ----------
    item : pygame.sprite.GroupSingle
        The object that is being checked for collision with mouse.
        
    Returns
    -------
    bool
        Whether or not mouse intercepts visible pixels in the pygame object.   
    '''
    mouse_pos = pygame.mouse.get_pos()
    mouse_mask = pygame.mask.from_surface(pygame.Surface((1, 1), pygame.SRCALPHA))  # Create a mask for the mouse cursor
    mouse_mask.set_at((0, 0), 1)  # Set a single pixel in the mask

    surface_mask = pygame.mask.from_surface(item.sprite.image)

    return surface_mask.overlap(mouse_mask, (mouse_pos[0] - item.sprite.rect.left, mouse_pos[1] - item.sprite.rect.top))
