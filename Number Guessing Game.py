n = 10  #number which is to be guessed

guesses = 1

print("Total number of times we can guess the number = 5 \n")

while(guesses<=5):

    number = int(input('Guess the number : '))

    if (number < n) :
        print("number should be less than the entered number.\n")

    elif (number > n) :
        print("number should be greater than the entered number.\n")

    else:
        print("you guessed the correct number. \n\nYou Won!!!")
        break

    print("number of guesses left : " , (5 - guesses) , '\n')   
    guesses = guesses + 1

if(guesses>5):
    print("No more guesses left. \n\nYou lost!!!")