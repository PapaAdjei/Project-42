import random
dictionary = {"Apple": "Usually round,red or green, edible fruit of a small tree",
              "Banana": "a tropical plant with a reddish or yellowish rind cultivated for their nutritious fruit",
              "Orange": "a globose,reddish-yellow,bitter or sweet,edible citrus fruit",
              "Pineapple": "the edible juicy, collective fruit of a tropical plant,that develops from a head of flowers and is surmounted by a crown of leaves",
              "Pawpaw": "large melon like furit of a tropical plant eaten raw or cooked"}
words = list(dictionary.keys())
clues = list(dictionary.values())
word = random.choices(words)
clue = random.choices(clues)

words == clues
word == clue


print(*clue,sep =",")
print(*word,sep=",")
guessed_word = input("Guess the word: ")

if guessed_word == word:
    print("You Won")

elif guessed_word != word:
    print("You lost")







"""
[word, clue] = ["apple", "What is red"]
word == clue

print(clue)
guessed_word = input("Guess the word: ")

if guessed_word == word:
    print("You Won")

elif guessed_word != word:
    print("You lost")"""
    
