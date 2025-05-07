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
