import random
import time

def sleep_delay():
    time.sleep(1)
    
# === Calculator ===
def Calculator(x, y):
    while True:
        print("\n=== Python Calculator ===")
        print("a. Add")
        print("b. Subtract")
        print("c. Multiply")
        print("d. Divide")
        print("e. Exit to Main Menu")
        
        choice = input("Enter your operation (letter or full text): ").strip().lower()
        
        if choice in ('a', 'add'):
            print(f"Adding {x} and {y}...")
            sleep_delay()
            result = x + y
            print(f"The sum of {x} and {y} is {result}")
        
        elif choice in ('b', 'subtract'):
            print(f"Subtracting {x} and {y}...")
            sleep_delay()
            result = x - y
            print(f"The difference of {x} and {y} is {result}")
        
        elif choice in ('c', 'multiply'):
            print(f"Multiplying {x} and {y}...")
            sleep_delay()
            result = x * y
            print(f"The product of {x} and {y} is {result}")
        
        elif choice in ('d', 'divide'):
            if y == 0:
                sleep_delay()
                print("Error! Cannot divide by zero")
            else:
                print(f"Dividing {x} by {y}...")
                sleep_delay()
                result = x / y
                print(f"The quotient of {x} and {y} is {result}")
        
        elif choice in ('e', 'exit to main menu'):
            print("\nThank you for using the Calculator. Returning to Main Menu.")
            break
        
        else:
            print("Invalid input, please enter a valid option!")
            
# === Temperature Converter ===
def TemperatureConverter(x):
    while True:
        print("\n=== Python Temperature Converter ===")
        print("a. Convert Celsius to Fahrenheit")
        print("b. Convert Fahrenheit to Celsius")
        print("c. Exit to Main Menu")

        choice = input("Enter your operation (letter or full text): ").strip().lower()
        
        if choice in ('a', 'convert celsius to fahrenheit'):
            print(f"Converting {x} °C to Fahrenheit...")
            sleep_delay()
            f = (9/5) * x + 32
            print(f"{x} °C is {f:.2f} °F")
        
        elif choice in ('b', 'convert fahrenheit to celsius'):
            print(f"Converting {x} °F to Celsius...")
            sleep_delay()
            c = (5/9) * (x - 32)
            print(f"{x} °F is {c:.2f} °C")
        
        elif choice in ('c', 'exit to main menu'):
            print("\nThank you for using the Temperature Converter. Returning to Main Menu.")
            break
        
        else:
            print("Invalid input, please enter a valid option!")
# === To-Do-List ===
def ToDoList():
    tasks = []
    while True:
        print("\n=== Python To-Do List ===")
        print("a. Add Task")
        print("b. Remove Task")
        print("c. View Tasks")
        print("d. Exit to Main Menu")
    
        choice = input("Enter your operation (letter or full text): ").strip().lower()
        
        if choice in ('a', 'add task'):
            task = input("Enter task name: ").strip()
            tasks.append(task)
            print(f"'{task}' successfully added.")
        
        elif choice in ('b', 'remove task'):
            task = input("Enter task name to remove: ").strip()
            if task in tasks:
                tasks.remove(task)
                print(f"'{task}' successfully removed.")
            else:
                print(f"Task '{task}' not found.")
        
        elif choice in ('c', 'view tasks'):
            print("\n--- Current Tasks ---")
            if tasks:
                for idx, t in enumerate(tasks, 1):
                    print(f"{idx}. {t}")
            else:
                print("No tasks yet.")
        
        elif choice in ('d', 'exit to main menu'):
            print("\nThank you for using the To-Do List. Returning to Main Menu.")
            break
        
        else:
            print("Invalid input, please enter a valid option!")

# === Number Guessing Game ===
def NumberGuessingGame():
    while True:
        print("\n=== Python Number Guessing Game ===")
        print("a. Play Number Guessing Game")
        print("b. Exit to Main Menu")
        
        choice = input("Enter your operation (letter or full text): ").strip().lower()
        
        if choice in ('a', 'play number guessing game'):
            number = random.randint(1, 100)
            guesses = 0
            while True:
                guess_str = input("Guess the lucky number (1–100): ").strip()
                if not guess_str.isdigit():
                    print("Please enter a number!")
                    continue
                guess = int(guess_str)
                guesses += 1
                print("Checking your answer...")
                sleep_delay()
                if guess > number:
                    print("Too high!")
                elif guess < number:
                    print("Too low!")
                else:
                    print(f"Correct! The number was {number}.")
                    print(f"It took you {guesses} guesses.")
                    break
        
        elif choice in ('b', 'exit to main menu'):
            print("\nThank you for playing. Returning to Main Menu.")
            break
        
        else:
            print("Invalid input, please enter a valid option!")

# === Student Grade Calcultor ===
def StudentGradeCalculator():
    scores = []
    while True:
        print("\n=== Python Student Grade Calculator ===")
        print("a. Add Score")
        print("b. Calculate Average")
        print("c. View Grades")
        print("d. Exit to Main Menu")
        
        choice = input("Enter your operation (letter or full text): ").strip().lower()
        
        if choice in ('a', 'add score'):
            subject = input("Enter subject name: ").strip()
            try:
                grade = float(input(f"Enter grade for {subject}: "))
                scores.append((subject, grade))
                print(f"Recorded: {subject} – {grade}")
            except ValueError:
                print("Please enter a numeric grade!")
        
        elif choice in ('b', 'calculate average'):
            if not scores:
                print("No scores to average.")
            else:
                print("\n--- Scores ---")
                for subj, gr in scores:
                    print(f"{subj}: {gr}")
                print("Calculating the average...")
                sleep_delay()
                avg = sum(gr for _, gr in scores) / len(scores)
                print(f"\nAverage grade: {avg:.2f}")
        
        elif choice in ('c', 'view grades'):
            print("\n--- Grades ---")
            if scores:
                for subj, gr in scores:
                    print(f"{subj}: {gr}")
            else:
                print("No grades recorded.")
        
        elif choice in ('d', 'exit to main menu'):
            print("\nThank you for using the Grade Calculator. Returning to Main Menu.")
            break
        
        else:
            print("Invalid input, please enter a valid option!")

# === Main Menu ===
while True:
    print("\n=== Main Menu ===")
    print("1. Calculator")
    print("2. Temperature Converter")
    print("3. To-Do List")
    print("4. Number Guessing Game")
    print("5. Student Grade Calculator")
    print("6. Exit Program")

    choice = input("Select an option (number or full text): ").strip().lower()
    if choice in ('1', 'calculator'):
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            Calculator(x, y)
        except ValueError:
            print("Please enter valid numbers!")
    elif choice in ('2', 'temperature converter'):
        try:
            x = float(input("Enter initial temperature: "))
            TemperatureConverter(x)
        except ValueError:
            print("Please enter a valid temperature!")
    elif choice in ('3', 'to-do list'):
        ToDoList()
    elif choice in ('4', 'number guessing game'):
        NumberGuessingGame()
    elif choice in ('5', 'student grade calculator'):
        StudentGradeCalculator()
    elif choice in ('6', 'exit program'):
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid input, please choose 1–6 or the full command.")
