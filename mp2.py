import random

def Calculator(x, y):
    while True:
        print("")
        print(" === Python Calculator === \n")
        print("a. Add")
        print("b. Subtract")
        print("c. Multiply")
        print("d. Divide")
        print("e. Exit to Main Menu")
        
        choice = input("Enter your operation (enter letter of operation): ")
        
        if choice in ['a' or 'Add']:
            print(f"Adding {x} and {y} ")
            sum = x + y
            print(f"The sum of {x} and {y} is {sum}")
        
        elif choice in ['b' or 'Subtract']:
             print(f"Subtracting {x} and {y} ")
             difference = x - y 
             print(f"The difference of {x} and {y} is {difference}")

        elif choice in ['c' or 'Multiply']:
             print(f"Multiplying {x} and {y} ")
             product = x * y 
             print(f"The product of {x} and {y} is {product}")
        
        elif choice in ['d' or 'Divide']:
             if y == 0.0:
                  print("Error! Cannot divide by zero")
             else:
                print(f"Dividing {x} and {y} ")
                product = x * y 
                print(f"The quotient of {x} and {y} is {product}")
        elif choice in ['e' or 'Exit to Main Menu']:
            print("")
            print("Thank You for using Python Calculator")
            print("Returning to Main Menu")
            break
        else:
            print("Invalid input, please enter two valid numbers!")

def TemperatureConverter(x):
    while True:
        print("")
        print(" === Python Temperature Converter === \n")
        print("a. Convert Celsius to Fahrenheit")
        print("b. Convert Fahrenheit to Celsius")
        print("c. Exit to Main Menu")

        choice = input("Enter your operation (enter letter of operation): ")
        if choice in ['a' or 'Convert Celsius to Fahrenheit']:
            print(f"Converting {x} °C to Fahrenheit ")
            fahrenheit = (((9/5) * x) + 32)
            print(f"{x} °C to Fahrenheit is {fahrenheit}°F")

        elif choice in ['b' or 'Convert Celsius to Fahrenheit']:
            print(f"Converting {fahrenheit} °F to Celsius ")
            celsius = ((5/9) * (fahrenheit - 32))
            print(f"{fahrenheit} °C to Fahrenheit is {celsius:.2f}°C")

        elif choice in ['c' or 'Exit to Main Menu']:
            print("")
            print("Thank You for using Python Temperature Converter")
            print("Returning to Main Menu")
            break
        else:
            print("Invalid value for temperature! Please reenter a value: ")





def ToDoList(): 
    tasks = []
    task = ""
    while True:
        print("")
        print(" === Python To-Do-List === \n")
        print("a. Add Task")
        print("b. Remove Task")
        print("c. View Tasks")
        print("d. Exit to Main Menu")
    
        choice = input("Enter your operation (enter letter of operation): ")
        
        if choice in ['a' or "Add Task"]:
            task = input("Enter task name: ")
            tasks.append(task)
            print(f"{task} successfully added to To-Do-List")
            
        elif choice in ['b' or "Remove Task"]:
             taskToRemove = input("Enter task name to remove: ")
             tasks.remove(taskToRemove)
             print(f"{taskToRemove} successfully added from To-Do-List")
             
        elif choice in ['c' or 'View Tasks']:
            print("")
            print("=== Tasks === \n")
            for i in tasks:
                print(i)
        elif choice in ['d' or 'Exit to Main Menu']:
            print("")
            print("Thank You for using Python To-Do-List")
            print("Returning to Main Menu")
            break 
        else:
            print("Invalid Task Description! Please reenter another one: ")


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
            
def StudentGradeCalculator():
    scores = []
    subjectCount = 0
    average = 0
    while True:
        print("")
        print(" === Python Student Grade Calculator === \n")
        print("a. Add Score")
        print("b. Calculate Average")
        print("c. View Grades")
        print("d. Exit to Main Menu")
        
        choice = input("Enter your operation (enter letter of operation): ")
        
        if choice in ['a' or 'Add Score']:
            subject = input("Input Subject: ")
            grade = int(input(f"Enter grade for {subject}: "))
            subjectCount += 1
            average += grade
            scores.append(f"{subject}, Grade: {grade} ")
                
        elif choice in ['b' or 'Calculate Average']:
            print("Calculating average given records below: \n")
            for i in scores:
                print(i)
            print("\n")
            average = average / subjectCount
            print(f"Your Average Grade is: {average:.2f}")
            
        elif choice in ['c' or 'View Grades']:
            print("")
            print(" === Grades === \n")
            for i in scores:
                print(i)
            print("\n")
            
        elif choice in ['d' or 'Exit to Main Menu']:
            print("Thank You for using Python Grade Average Calculator")
            print("Returning to Main Menu")
            break
        
        else:
            print("Invalid Input! Please reenter another one: ")
            
while True:
    print("\n=== Main Menu ===")
    print("1. Calculator")
    print("2. Temperature Converter")
    print("3. To-Do-List")
    print("4. Number Guessing Game")
    print("5. Student Grade Calculator")
    print("6. Exit Program")

    choice = input("Select an option: ").strip()
    if choice in ['1' or 'Calculator']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    
        Calculator(x, y)
        choice = input("Do you want to try again? 1 for yes 0 for no: ")
    
        if choice == '1':
             continue
     
        else:
             print("Exiting Program")
             break

    elif choice in ['2' or 'Temperature Converter']:
        x = float(input("Enter temperature in °C: "))
        TemperatureConverter(x)
        choice = input("Do you want to try again? 1 for yes 0 for no: ")
        if choice == '1':
             continue
        else:
             print("Exiting Program")
             break
        
    elif choice in ['3' or 'To-Do-List']:
        ToDoList()
        choice = input("Do you want to try again? 1 for yes 0 for no: ")
        if choice == '1':
             continue
        else:
             print("Exiting Program")
             break
        
    elif choice in ['4' or 'Number Guessing Game']:
           NumberGuessingGame()
           choice = input("Do you want to try again? 1 for yes 0 for no: ")
           if choice == '1':
              continue
           else:
              print("Exiting Program")
              break
        
    elif choice in ['5' or 'Student Grade Calculator']:
        StudentGradeCalculator()
        choice = input("Do you want to try again? 1 for yes 0 for no: ")
        if choice == '1':
            continue
        else:
            print("Exiting Program")
            break
        
    elif choice in ['6' or 'Exit Program']:
        print("Exiting Program...")
        break
    else:
        print("Invalid input. Try again.")
'''
while True:
    StudentGradeCalculator()
    choice = input("Do you want to try again? 1 for yes 0 for no: ")
    if choice == '1':
        continue
    else:
        print("Exiting Program")
        break
        
        
        
'''          

    
'''
while True:
    NumberGuessingGame()
    choice = input("Do you want to try again? 1 for yes 0 for no: ")
    if choice == '1':
        continue
    else:
        print("Exiting Program")
        break
'''

        

'''
while True:
    ToDoList()
    choice = input("Do you want to try again? 1 for yes 0 for no: ")
    if choice == '1':
        continue
    else:
        print("Exiting Program")
        break
'''          

''' 
while True:
    x = float(input("Enter temperature in °C: "))
    TemperatureConverter(x)
    choice = input("Do you want to try again? 1 for yes 0 for no: ")
    if choice == '1':
        continue
    else:
        print("Exiting Program")
        break
'''


'''
while True:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
    Calculator(x, y)
    choice = input("Do you want to try again? 1 for yes 0 for no: ")
    
    if choice == '1':
        continue
    else:
        print("Exiting Program")
        break


'''

