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
