import random

# create a list of 5 fruits...
word_list = ['apple', 'banana', 'grape', 'peach', 'carrot']
print(word_list)
word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess.isalpha:
    print("Good guess!")
else:
    print("That's not a valid input.")


#print(guess.isalpha())
