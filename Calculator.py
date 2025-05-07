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
