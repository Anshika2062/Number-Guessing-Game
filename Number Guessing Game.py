# NUMBER GUESSING GAME!!!

import random

print("WELCOME TO NUMBER GUESSING GAME!!!!\n\n")


# Generate a random number within the specified range

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))


n = random.randint(lower_bound, upper_bound)

print(f"\nI have chosen a number between {lower_bound} and {upper_bound}.\n")



guesses = 1

print("Total number of times we can guess the number = 5 \n")

while(guesses<=5):

    number = int(input('Guess the number : '))

    if (number > n) :
        print("number should be less than the entered number.\n")

    elif (number < n) :
        print("number should be greater than the entered number.\n")

    else:
        print("you guessed the correct number. \n\nYou Won!!!")
        break

    print("number of guesses left : " , (5 - guesses) , '\n')   
    guesses = guesses + 1

if(guesses>5):
    print("No more guesses left. \n\nYou lost!!!")