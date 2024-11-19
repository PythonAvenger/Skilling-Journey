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

# URGENT: Input the image index for each plot
plots = {
    "basic_plot": {
        "stats" : {},
        "image_index": "../assets/images/skills/",
        "available_paths": 3,
        "next_upgrades": ["fertilized_plot", "irrigated_plot", "enchanted_plot"]
    },
    # The rest after basic plot most likely wont have stats but a stat threshold
    # Stat threshold being the stat requirement for the fence to update it's look
    # This or use some sort of currency to upgrade plot
    "fertilized_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 1,
        "next_upgrades": ["nutrient_rich_plot"]
    },
    "irrigated_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 1,
        "next_upgrades": ["protected_plot"]
    },
    "enchanted_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 1,
        "next_upgrades": ["herbal_plot"]
    },
    "nutrient_rich_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 2,
        "next_upgrades": ["advanced_plot", "organic_plot"]
    },
    "protected_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 2,
        "next_upgrades": ["eco_friendly_plot", "hybrid_plot"]
    },
    "herbal_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 2,
        "next_upgrades": ["experimental_plot", "industrialized_plot"]
    },
    "advanced_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 2,
        "next_upgrades": ["high_tech_plot", "precision_plot"]
    },
    "organic_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 2,
        "next_upgrades": ["sustainable_plot", "compost_plot"]
    },
    "eco_friendly_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 2,
        "next_upgrades": ["solar_powered_plot", "rainwater_harvesting_plot"]
    },
    "hybrid_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 2,
        "next_upgrades": ["gmo_plot", "crossbreed_plot"]
    },
    "experimental_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 2,
        "next_upgrades": ["research_plot", "trail_plot"]
    },
    "industrialized_plot": {
        "stat_threshold": {},
        "image_index": "../assets/images/skills/",
        "available_paths": 2,
        "next_upgrades": ["tech_enhanced_plot", "automated_plot"]
    },
    "high_tech_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "precision_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "sustainable_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "compost_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "solar_powered_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "rainwater_harvesting_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "gmo_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "crossbreed_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "research_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "trail_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "tech_enhanced_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    },
    "automated_plot": {
        "image_index": "../assets/images/skills/",
        "available_paths": 0,
    }
}

class FarmPlot(pygame.sprite.Sprite): # TODO: Rework FarmPlot
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
    
