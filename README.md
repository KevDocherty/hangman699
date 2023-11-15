# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

# Milestone_3
There are 2 functions:
- ask_for_input()
  This prompts the user for a letter, and saves it to a variable called 'guess'
- check_guess(guess)
  This checks whether the guess is in the word

# Milestone_4
Created a 'Hangman' class, taking word_list (list of strings) and num_lives (int)
as parameters, where num_lives takes a default value of 5.

The computer makes a random choice from the word_list and allocates it to the attibute 'word'.

Added the 'ask_for_input()' and 'check_guess()' methods to the class.

An attribute 'word_guessed' is initialised as a list of underscores ('_') of the
same length as the 'word' attribute. Each time the user correctly guesses a letter,
the corresponding underscore is replaced by the letter. If an incorrect guess is made,
the num_lives is decremented.

# Milestone_5
Put all the previous code milestones together to implement a working version of the game.
