'''
Classes and functions involving the agronomy skill
'''

# TODO 1: Plan agronomy skill more and create pixel art for it.

import pygame
from pygame.sprite import _Group

animal_base_stats = {
    "chicken": {
        "stats": {
            "production": 1,
            "speed": 5,
            "mood": 1,
        },
        "produce": {
             "eggs": 3,
             "feather": 1
        }
    },
    "cow" : {
        
    }
}

fences = {
    "broken_down_fence": {
        "stats" : {},
    },
    "wooden_fence": {
        
    },
    "reinforced_wooden_fence": {
        
    },
    "copper_fence": {
        
    }
}

plots = {
    "dirt_plot": {
        "stats" : {},
        "image": "../assets/images/skills/"
    },
    # The rest after this most likely wont have stats but a stat threshold
    # Stat threshold being the stat requirement for the fence to update it's look
    "enriched_plot": {
        "stat_threshold": {},
        "image": "../assets/images/skills/"
    },
    "mutated_plot": {
        
    },
    "---------_plot": {
        
    }
}

class FarmPlot(pygame.sprite.Sprite):
    def __init__(self, plots: dict[str: dict] = plots):
        super().__init__()
        self.plots = plots
        
        self.name = self.plots.keys()[0]
        self.stats: dict = self.plots[self.name]["stats"]
        
        self.image = pygame.image.load([self.plots[self.name]["image"]]).convert_alpha()
        self.rect = self.image.get_rect()
        
        
    def can_upgrade(self):
        next_plot_stat_requirements = self.plots[self.plots.keys()[[self.plots.keys()].index(self.name) + 1]]["stat_threshold"]
        for stat in self.stats.keys():
            if self.stats[stat] < next_plot_stat_requirements[stat]:
                return False
        return True
    
    def upgrade_plot(self, stat: str): #TODO: Finish Upgrade_Plot
        pass
    
    def visual_upgrade(self):
        self.image = pygame.image.load(self.plots[self.plots.keys()[[self.plots.keys()].index(self.name) + 1]]["image"]).convert_alpha()
        self.rect = self.image.get_rect()
        
    def update(self):
        if self.can_upgrade():
            self.visual_upgrade()


# TODO: Work on Crop class
class Crop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

# TODO: Work on Animal class
class Animal(pygame.sprite.Sprite):
    def __init__(self):
        pass


# TODO: Work on Fence class
class Fence(pygame.sprite.Sprite):
    def __init__(self):
        pass
    
