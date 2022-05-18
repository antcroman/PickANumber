import random
import time

play_game = 1

#1.1
def number_validation(x):
    global check_pass                                               #validates users input to verify it is a number
    if x.strip().isdigit():
        check_pass = 1
    else:
        print("Input is not a number")


#1.2
def range_validation(x, y):                                            #validates users input to verify it is in an appropriate range
    if x < y:
        return
    else:
        print("Input range is not valid")
        number_declaration()


#1
def number_declaration():                                                       #obtains users input
    global min_value
    global max_value
    global check_pass
    check_pass = 0

    while check_pass == 0:                                                      #loops prompting for a value when the value check fails
        min_value = (input("Please enter a minimum value number (inclusive): "))
        number_validation(min_value)

    check_pass = 0
    min_value = int(min_value)

    while check_pass == 0:                                                      #loops prompting for a value when the value check fails
        max_value = (input("Please enter a maximum value number (inclusive): "))
        number_validation(max_value)

    max_value = int(max_value)
    range_validation(min_value, max_value)



#2
def number_generator():
    global random_number

    random_number = random.randint(int(min_value), int(max_value))              #generate random number for the game


#3.1
def guess_validation(x):                                                        #validates users guess to be within specified range and ensures it is a number
    global guess_verified_num
    guess_verified_num = 0

    while guess_verified_num == 0:
        if x.strip().isdigit():
            guess_verified_num = 1

            if int(x) < min_value:
                print("Input is lower than minimum number")
                obtain_guess()
            if int(x) > max_value:
                print("Input is higher than minimum number")
                obtain_guess()

        else:
            print("Input is not a number")
            obtain_guess()


#3
def obtain_guess():                                                             #obtains guess from user and then validates it
    global user_guess

    user_guess = input("Guess the number between: " + str(min_value) + ' and ' + str(max_value) + ': ')    #obtains user input
    guess_validation(user_guess)
    user_guess = int(user_guess)


#4
def compare_numbers(x, y):                                                      #compares guessed number with generated number
    if x == y:
        print("You are correct")
        print("random number is " + str(y))
    else:
        print("You are incorrect")
        print("random number is " + str(y))


#5
def play_again():
    global desicion
    global play_game
    desicion = 0

    while desicion == 0:                                                        #loop stops user from trying to break game with incorrect input
        play_again = (input("play again? (y/n): "))
        if play_again == "y" or play_again == "Y":                              #restarts gane by restarting main loop and resetting key game variables
            desicion = 1
        elif play_again == "n" or play_again == "N":                            #breaks out of main game loop to finish program
            desicion = 1
            play_game = 0
        else:
            print("Please enter a valid input, play again? (y/n): ")




#--------------Start of game----------------------------------------------------

print("Welcome to the number guesser")

while play_game == 1:                                   #this determines if game will loop based on users desicion in play_again() (whole game encompased in this while loop)                                                #loop stops user from trying to break game with incorrect input

    number_declaration()

    number_generator()

    obtain_guess()

    compare_numbers(user_guess, random_number)

    play_again()

print("Thank you for playing")
