#Firstly, i created an empty list where all my tasks will be stored to 
tasks = []

#Now i created the functions individually as created above
def add_task():
    task = input("Enter a task: ")
    tasks.append({"Task": task, "Status": "pending"});
    print("New task added successfully \n")

def view_task():
    print("Your To-do list")
    if len(tasks) == 0:
        print("No pending tasks")
    else: 
        for index, task in enumerate(tasks, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")

def remove_task():
    if len(tasks) == 0:
        print("List is empty\n")
    else:
        try:
            search_index = int(input("Enter the task number you want to remove: ")) - 1
            if 0 <= search_index < len(tasks):
                removed_task = tasks.pop(search_index)
                print(f"Task removed: {removed_task['Task']}")
            else:
                print("Invalid task number\n")
        except ValueError:
            print("Please enter a valid task number")


def mark_task():
    if len(tasks) == 0:
        print("List is totally empty")
    else: 
        try:
            search_index = int(input("Enter the task number you want to mark as complete: \n")) - 1
            if 0 <= search_index < len(tasks):
                if tasks[search_index]['Status'] =='Done':
                     print(f"Task '{tasks[search_index]['Task']}' has be already been marked done\n")
                else:
                    tasks[search_index]['Status'] = 'Done'
                    print(f"Task {tasks[search_index]['Task']} has been completed")
            else:
                    print("Invalid task number\n")
           
        except ValueError:
               print("Please enter a valid task number")
        

#Then i defined a function to display my menu and use a while 
# loop for it to continue showing until a condition is met
def menu():
    while True:
        print("--- Main Menu---")
        print("1. Add a new task")
        print("2. View all task")
        print("3. Remove all task")
        print("4. Mark a task as complete")
        print("5. Exit")

#Here, i will ask the user to input the choice of option from the above listed

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            mark_task()
        elif choice == 5:
            print("Exisiting application")
            exit()
        else:
            print("Invalid option selected, please try again")

menu()