import random

def NumberGuessingGame():
    guesses = 1
    while True:
        print("")
        print(" === Python Number Guessing Game === \n")
        print("a. Play Number Guessing Game")
        print("b. Exit to Main Menu")
        
        choice = input("Enter your operation (enter letter of operation): ")
        if choice in ['a' or 'Play Number Guessing Game']:
            number = random.randint(1, 100)
            while True:     
                guess = input("Guess the lucky number between (1 - 100): ")
                if guess.isdigit():
                     guess = int(guess)
                     if guess > number:
                           print("Too High")
                           guesses += 1
                     elif guess < number:
                          print("Too Low")
                          guesses += 1
                     elif guess == number:
                          print(f"Correct! The Number was {number}")
                          print(f"It took you {guesses} number of guesses")
                          break
                     else:
                          print("Invalid Operation! Please reenter another one: ")
                else:
                     print("Invalid Operation! Please reenter another one: ")
                    
        elif choice in ['b' or 'Exit to Main Menu']:   
            print("Thank You for using Python Number Guessing Game")
            print("Returning to Main Menu")
            break
        
        else:
            print("Invalid Input! Please reenter another one: ")