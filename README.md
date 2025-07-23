# Hangman
1. What You’re Building
Create your own Hangman game in Python. The computer secretly chooses a word; the player guesses one letter at a time. After six wrong guesses, the little stick-figure is fully “hung” and the game ends. You will extend the starter code we’ve provided.
2. Core Requirements (scoreable items)
#
Must-Have Feature
Why It Matters
1
Word List & Random Choice – program selects a secret word from word_list.
Ensures replay value.
2
Letter Input – capture one keystroke at a time with pygame.KEYDOWN.
Introduces real-time event handling.
3
Variable Tracking – use ≥ 3 variables (game_word, guessed, hangman_mistakes, …).
Meets learning goal on variables & data types.
4
Conditional Logic – if / elif / else decides whether a guess is correct and when the game is over.
Aligns with the conditionals' objective.
5
Win / Lose Feedback – display “YOU WON” or “YOU LOST” plus the correct word.
Provides closure for the player.
6
Visual Update – swap to the next image in images[] each time hangman_mistakes increments.
Connects logic to graphics.

Checklist for success: If your game runs cleanly, updates the picture, and prints a win/lose message after guessing, you’ve met the six core requirements.
