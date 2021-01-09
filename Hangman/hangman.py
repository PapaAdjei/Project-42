# importing libraries
import random
import math

# printing introductory messages
print("\tWelcome to Hangman(Guess the word game)!")
print("\nYou have", round(math.log(8-1+1, 2)),
      "chances to guess the right letters to form a word")


# clues and  words in a dictionary
dictionary = {"Apple": "Usually round,red or green, edible fruit of a small tree",
              "Banana": "a tropical plant with a reddish or yellowish rind cultivated for their nutritious fruit",
              "Orange": "a globose,reddish-yellow,bitter or sweet,edible citrus fruit",
              "Pineapple": "the edible juicy, collective fruit of a tropical plant,that develops from a head of flowers and is surmounted by a crown of leaves",
              "Pawpaw": "large melon like furit of a tropical plant eaten raw or cooked"}

# list of words from the dictionary
words = list(dictionary.keys())

# list of clues from the dictionary
clues = list(dictionary.values())

#equalling words in the list of words 
words == clues
# choosing a random word from the list of words
word = random.choice(words)

# selecting a random clue from the list of clues
clue = random.choice(clues)

# for storing the guessed word
guessed_word = ""

# Number of chances to guess the word
chances = round(math.log(8-1+1, 2))

while True:
    # prints a clue to help guess a word
    print("\n\t", clue)

    # number of chances a user can use in guessing a word
    chances > 0

    # counts the number of times a user failed
    fails = 0

    # a loop for checking user inputs
    for char in word:
        # for equalling the clue to its word
        word == clue
       # condition to compare the characters with the characters in the guess
        if char in guessed_word:
            print(char)

        else:
            print("\t_")

            fails += 1
    # condition for comparing if a user failed
    if fails == 0:
        print("You win")

        # print the correct word
        print("The word is: ", word)

        break

    guess = input("Guess the word: ")

    #storing every input guessed character
    guessed_word += guess

    #checking input
    if guess not in word:
        chances -= 1
        print("Wrong")

        print("You have",+ chances,"chances")  


        if chances == 0:
            print("You loose")

    
    continue

   
