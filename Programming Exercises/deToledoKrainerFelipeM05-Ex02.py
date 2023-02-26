# importing random number
import random

number = random.randint(1, 100)


# creating function
def main():
    print("This is a number guessing game.")
    print("Guess what number we thought of between 1 and 100")

    num = number

    # stores user input
    user = 0

    # stores number of guesses
    guess = 0

    # Receiving input
    user = int(input("Enter your best guess: "))

    # while statement
    while user != num:

        # adding to the guess counter
        guess = guess + 1

        # checking if input is greater or lower and printing.
        if user > num:

            print("Too high, try again")

        # else
        else:

            print("Too low, try again")

        # receiving input
        user = int(input("Enter your best guess: "))

    # printing final answer
    print("Congrats, you won!")
    print("Restarting game")
    print("Number of guesses are", guess)
    main()


# making function call to main
main()
