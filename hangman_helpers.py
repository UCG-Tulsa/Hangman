import pygame
import random

def setup_game(window_width=1000, window_height=400):
    """Initialize the game window and basic elements"""
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Hangman")
    return window

def load_images():
    """Load all the hangman images"""
    images = []
    for i in range(1, 8):
        image = pygame.image.load(f"man{i}.png")
        images.append(image)
    return images

def pick_word(word_list=None):
    """Pick a random word from the list"""
    if word_list is None:
        word_list = ["python", "game", "code", "fun", "learn"]
    return random.choice(word_list)

def create_text(text, size=40, color='black'):
    """Create a text surface"""
    font = pygame.font.SysFont("comicsans", size)
    return font.render(text, True, color)

def draw_game(window, images, mistakes, word, guessed, width=1000):
    """Draw everything on the screen"""
    window.fill('white')

    # Draw title
    title = create_text("The Big 3", 70)
    window.blit(title, (width/2 - title.get_width()/2, 10))

    # Draw word with blanks
    display_word = ""
    for letter in word:
        display_word += letter + " " if letter in guessed else "_ "
    word_text = create_text(display_word)
    window.blit(word_text, (500, 250))

    # Draw hangman image
    window.blit(images[mistakes], (50, 50))
    pygame.display.update()

def check_win(word, guessed):
    """Check if player has guessed all letters"""
    return all(letter in guessed for letter in word)

def show_result(window, message, color, width=1000, height=400):
    """Show win/lose message"""
    window.fill('white')
    text = create_text(message, 40, color)
    window.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
