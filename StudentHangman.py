from hangman_helpers import *

# CREATE GAME WINDOW/SCREEN
# HINT: use a function from the list


# LOAD GAME PICTURES
# HINT: use a function from the list


# CREATE LIST OF AT LEAST 10 WORDS


# PICK A RANDOM WORD
# HINT: use a function from the list


# KEEP TRACK OF GAME
# What are two variables we can use to keep track of our progress in the game


# NAME THE GAME


# PLAY UNTIL WE TELL IT TO STOP
playing = True

while playing:
    # WHAT DO WE SEE ON THE SCREEN
    # HINT: use a function from the list

    for event in pygame.event.get():
        # CLOSE THE GAME
        # IF WINDOW IS CLOSED
        if event.type == pygame.QUIT:
            # STOP PLAYING
            playing = False

        # DETECT KEY
        if event.type == pygame.KEYDOWN:
            key = event.unicode.lower() # Grab unicode of pressed key

            # IF THE KEY PRESSED HAS NOT BEEN TRIED BEFORE

                # ADD IT TO THE LIST OF GUESSED KEYS

                #IF THAT KEY WAS WRONG

                    # INCREASE THE COUNT ON THE AMOUNT OF MISTAKES

    # CHECK FOR WIN
    # HINT: use a function from the list


    # IF WE WON:

        # CELEBRATION MESSAGE (HINT: use a function from the list)

        # STOP PLAYING


    # IF WE DID NOT WIN AND WE RAN OUT OF GUESSES (We only have 6)

        # TELL PLAYER THEY LOST (HINT: use a function from the list)

        # STOP PLAYING


pygame.quit()
