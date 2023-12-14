# Randy Jackson
# 12/7/23
# Math quiz, using functions, random numbers, and while loop
# will need to import random library

# will need a while loop for main code
# another loop for 
# need three funcions menu() add() subtract()

import random

# create menu function, this function 
def show_menu():
    print("Welcome to Math Quiz")
    print()
    print("Main Menu")
    print("_______________")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()

# This function adds two random numbers
def add():
    ran1 = random.randint(0,10)
    ran2 = random.randint(0,10)
    print(f"{ran1} + {ran2}")
    return (ran1 + ran2)

# This function subtracts two random numbers
def subtract():
    ran1 = random.randint(0,10)
    ran2 = random.randint(0,10)
    print(f"{ran1} - {ran2}")
    return (ran1 - ran2)

# This function simulates the user guessing.
# While the guess is wrong, allow the user to guess again

def guessing (guess, correct_answer):
    num_guesses = 0
    while guess != correct_answer:
        num_guesses += 1
        if guess > correct_answer: # If user guesses too high 
            print("Your guess is too high")
            guess = int(input("guess again"))# represents guess, give guess again
        else:                      # If user guesses too low
            print("Your guess is too low")
            guess = int(input("guess again"))# represents guess, gives the second option

    # user answer is correct, the while loop breaks
    print("your answer is correct!!!")
    print(f"It took you {num_guesses} incorrect guesses to get it right")



#get input from user



# Main Function all logic will go inside, that we wrote from the top
def main():
    show_menu()
    user_option = int(input("Please choose one of the menu options, 1, 2, 3: "))
    while user_option != 3:
        if user_option == 1:
            ran_sum = add() # represents the correct answer
            my_guess = int(input("What is your guess"))# represents guess
            print()
            guessing(my_guess, ran_sum)
            show_menu()
            user_option = int(input("Please choose one of the menu options, 1, 2, 3: "))

        if user_option == 2:
            ran_sum = subtract() # represents the correct answer
            my_guess = int(input("What is your guess"))# represents guess
            guessing(my_guess, ran_sum)
            show_menu()
            user_option = int(input("Please choose one of the menu options, 1, 2, 3: "))
        # if user_choice == 3, the while loop breaks
    print("Thank you for playing goodbye")


# call the main function
if __name__ == "__main__":
    main()