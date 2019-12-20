"""
Dobble game for children
"""

import pygame
import random

cards=[
        [0, 1, 2, 3, 4, 25],
        [5, 6, 7, 8, 9, 25],
        [10, 11, 12, 13, 14, 25],
        [15, 16, 16, 17, 19, 25],
        [20, 21, 22, 23, 24, 25],
        [0, 5, 10, 15, 20, 26],
        [1, 6, 11, 16, 21, 26],
        [2, 7, 12, 17, 22, 26],
        [3, 8, 13, 18, 23, 26],
        [4, 9, 14, 19, 24, 26],
        [0, 6, 12, 18, 24, 27],
        [1, 7, 13, 19, 20, 27],
        [2, 8, 14, 15, 21, 27],
        [3, 9, 10, 16, 22, 27],
        [4, 5, 11, 17, 23, 27],
        [0, 7, 14, 16, 23, 28],
        [1, 8, 10, 17, 24, 28],
        [2, 9, 11, 18, 20, 28],
        [3, 5, 12, 19, 21, 28],
        [4, 6, 13, 15, 22, 28],
        [0, 8, 11, 19, 22, 29],
        [1, 9, 12, 15, 23, 29],
        [2, 5, 13, 16, 24, 29],
        [3, 6, 14, 17, 20, 29],
        [4, 7, 10, 18, 21, 29],
        [0, 9, 13, 17, 21, 30],
        [1, 5, 14, 18, 22, 30],
        [2, 6, 10, 19, 23, 30],
        [3, 7, 11, 15, 24, 30],
        [4, 8, 12, 16, 20, 30],
        [25, 26, 27, 38, 29, 30]
        ]

settings = {
'screen_width': 1200,
'screen_height': 600,
'screen_bg_col': (255, 255, 255),
'maxfps': 30,
}


def card_generator(cards, number=2):
    """ Generates random cards for playing dobble

    cards - set of cards to choose from
    number - number of cards to choose (default=2)
    """
    return  random.sample(cards, number)

def load_image(number):
    """ Load and resize the surface image bound to a given
    card number """
    
    

def run_game():
    # Initialize pygame, settings and screen object
    pygame.init() 
    screen = pygame.display.set_mode(
            (settings['screen_width'], settings['screen_height'])) 
    pygame.display.set_caption("Dobble") 
    
    dont_burn_my_cpu = pygame.time.Clock()
    
    while True:
        screen.fill(settings['screen_bg_col'])
        pygame.display.flip()
        
        dont_burn_my_cpu.tick(settings['maxfps'])

run_game()