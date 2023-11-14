import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        #print(self.word)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(list(self.word)))
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()

        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word.")

            for letter, index in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[index] = letter
                else:
                    self.num_lives -= 1
                    print(f"Sorry, {letter} is not in the word.")
                    print(f"You have {self.num_lives} lives left.")

            self.num_letters -= 1


    def ask_for_input(self):
        # ask the user to guess a letter
        while True:
            self.guess = input("Please enter a single letter: ")
            if len(self.guess) != 1 and not (guess.isalpha):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)
                #print(self.list_of_guesses)




#check_guess(guess)
my_game = Hangman(['apple', 'banana', 'grape', 'peach', 'carrot'])
my_game.ask_for_input()
