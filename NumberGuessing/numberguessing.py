# importing libraries
import random
import math

# Function to validate Input


def ValidateInput(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("You didn't type a number")
            continue
        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


# Taking Input
lower = ValidateInput("Enter lower number: ")

upper = ValidateInput("Enter upper number: ")

# generating randm number between lower and upper bound
ran_guess = random.randint(lower, upper)
print("\n\t You have only", round(math.log(upper - lower + 1, 2)), "chances to guess the number\n")

# initializing the number of guesses
guess_count = 0

# calculation of minimum number of guesses depending on range
while guess_count < math.log(upper - lower + 1, 2):
    guess_count += 1

    # taking other guesses
    user_guess = ValidateInput("Guess a number: ")

    # condition testing
    if ran_guess == user_guess:
        print("You guessed correctly on your ", guess_count, "count")
        break
    elif ran_guess > user_guess:
        print("you guessed too small")
        continue
    elif ran_guess < user_guess:
        print("You guessed too high")
        continue

# controlling guesse count
if guess_count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % ran_guess)
    print("It was nice trying!")
