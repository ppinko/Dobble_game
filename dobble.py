"""
Dobble game for children
"""

import pygame
import sys
import random

cards = [
        [0, 1, 2, 3, 4, 25],
        [5, 6, 7, 8, 9, 25],
        [10, 11, 12, 13, 14, 25],
        [15, 16, 17, 18, 19, 25],
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
        [25, 26, 27, 28, 29, 30]
        ]

settings = {
'screen_width': 300,
'screen_height': 500,
'screen_bg_col': (255, 255, 255),
'maxfps': 30,
'game_active': False
}

class Button():

    def __init__(self, screen, msg):
        """Initilize button attributes"""
        #self.screen_width = settings['screen_width']
        #self.screen_height = settings['screen_height']
        self.screen_rect = screen.get_rect()
        self.screen = screen

        # Set the dimensions and properties of the button
        self.width, self.height = 100, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 20) # None - default font, 48 - size of the font

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self.prep_msg(msg)
                
    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                self.button_color) # True - antialiasing on
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

def card_generator(cards, number=2):
    """ Generates random cards for playing dobble

    cards - set of cards to choose from  
    number - number of cards to choose (default=2)

    return - list containing two cards
    """
    return  random.sample(cards, number)

def board(card_hand):
    """ Generate matrix with images and their positions 

    card_hand - result of card generator 
    return - matrix with numbers which corresponds to img
    """
    board = []
    board.append(card_hand[0][:3])
    board.append(card_hand[0][3:])
    board.append([-1, -1, -1])
    board.append(card_hand[1][:3])
    board.append(card_hand[1][3:])

    return board


def same_cards(card_hand, board):
    """
    Return which cards in the given set are the same

    Input:
    board - matrix with numbers

    Output:
    tuple containing indexes in the board with the same cards
    """
    hand_1 = card_hand[0]
    hand_2 = card_hand[1]

    for i, element in enumerate(hand_1):
        if element in hand_2:
            if i <= 2:
                first_img = (0, i)
            else:
                first_img = (1, i-3)
            
            index = hand_2.index(element)
            if index <= 2:
                second_img = (3, index)
            else:
                second_img = (4, index-3)

            return (first_img, second_img)


def img_rect(position):
    """
    """
    # Build the button's rect object and center it
    same_rect = pygame.Rect(0, 0, 80, 80)
    same_rect.center = (50 + 100 * position[1], 50 + 100 * position[0])
    print(same_rect.center)
    return same_rect


def load_image(number):
    """ Load and resize the surface image bound to a given
    card number """

    image = pygame.image.load('images/img_{0}.png'.format(number))
    scaled_image = pygame.transform.scale(image, (80, 80))    
    return scaled_image


def blitme(screen, scaled_image, rect):
    """ Draw image on the screen"""
    screen.blit(scaled_image, rect)


def draw_board(screen, board):
    """ 
    Draw a board with images

    screen - surface to draw on
    board - matrix with picture numbers
    """
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column >= 0:
                scaled_image = load_image(column)
                rect = scaled_image.get_rect()
                rect.center = (50 + 100 * j, 50 + 100 * i)
                blitme(screen, scaled_image, rect)


def check_events(game_button, settings, card_hand, new_board, screen):
    """Collects and checks events"""    
    for event in pygame.event.get():
        # Enables to close the game while clicking on the 'x'
        if event.type == pygame.QUIT:
            sys.exit() 
        
        # Mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            # gather position of the click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if settings['game_active'] == False:
                check_game_button(game_button, mouse_x, mouse_y, settings)
            else:
                print('Active game')
                t1 = same_cards(card_hand, new_board)
                print(t1)
                found_1 = img_rect(t1[0])
                found_2 = img_rect(t1[1])
                found_clicked_1 = found_1.collidepoint(mouse_x, mouse_y)
                found_clicked_2 = found_2.collidepoint(mouse_x, mouse_y)
                if found_clicked_1 or found_clicked_2:
                    print("HIT")
                    card_hand = card_generator(cards)
                    board_temp = board(card_hand)
                    new_board.clear()
                    new_board.extend(board_temp)
                    draw_board(screen, new_board)


def check_game_button(game_button, mouse_x, mouse_y, settings):
    """Check when player cliks start"""
    button_clicked = game_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        # Start the game
        settings['game_active'] = True

def run_game(settings):
    # Initialize pygame, settings and screen object
    pygame.init() 
    screen = pygame.display.set_mode(
            (settings['screen_width'], settings['screen_height'])) 
    pygame.display.set_caption("Dobble") 
    
    dont_burn_my_cpu = pygame.time.Clock()
    
    card_hand = card_generator(cards)
    new_board = board(card_hand)

    game_active = False
    game_button = Button(screen, 'Start')
    while True:
        screen.fill(settings['screen_bg_col'])
        if settings['game_active'] == False:
            game_button.draw_button()
            check_events(game_button, settings, card_hand, new_board, screen)
        else:
            draw_board(screen, new_board)
            check_events(game_button, settings, card_hand, new_board, screen)
        pygame.display.flip()   
        dont_burn_my_cpu.tick(settings['maxfps'])

run_game(settings)