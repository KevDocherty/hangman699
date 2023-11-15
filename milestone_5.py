import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        print(self.word)
        self.word_guessed = ['_' for letter in self.word]
        #self.num_letters = len(set(list(self.word)))
        self.num_letters = len(list(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        #print('inside check_guess')
        self.guess = guess.lower()
        #print(f'self.guess = {self.guess}')

        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[index] = letter
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {self.guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        print(f"You have correctly guessed the following: {self.word_guessed}")


    def ask_for_input(self):
        # ask the user to guess a letter
        #while True:
        self.guess = input("Please enter a single letter: ")
        if len(self.guess) != 1 or not self.guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif self.guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)
            #print(self.list_of_guesses)


def play_game(word_List):
    num_lives = 5
    game = Hangman(word_List, num_lives)

    while True:
        #print(game.num_lives)
        #print(game.num_letters)
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


#check_guess(guess)
word_list = ['apple', 'banana', 'grape', 'peach', 'carrot']
play_game(word_list)
