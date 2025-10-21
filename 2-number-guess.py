import random

max_number = input("Type a number: ")
if max_number.isdigit():
    max_number = int(max_number)

if max_number <= 0:
    print("Don't be so negative! Byeeee.")
    quit()

print("Thanks! I'm thinking of a number between 0 and", max_number, "...")

r = random.randint(0, max_number)

max_guesses = 20
num_guesses = 0
user_guess = ""
while num_guesses < max_guesses and user_guess != r:
    user_guess = input("What number am I thinking of?: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        num_guesses += 1
    else:
        print("No no... a number. Type a number!")

    if user_guess == r:
        print("You got it!")
        break
    else:
        print("Nope! Try again.")

print("Congrats! You got it in", num_guesses, "guesses!")
