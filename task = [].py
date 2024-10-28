task = []

def new_task():
    user_task = input("Enter task: ")
    task.append(user_task)

def note_task():
    view_task()
    select_task = int(input("Which task would you like to add a note to? "))
    note_task = str(input("Enter note: "))
    task[select_task-1] = task[select_task-1] +'  NOTE: '+ note_task

def view_task():
    for i, j in enumerate(task):
        print(i + 1, " ", j)


def complete_task():
    task_num = int(input("Enter task that you have completed: "))
    task.pop1(task_num - 1)
    view_task()


def show_menu():
    print("Welcome to your task manager!")
    print("1. Add new task")
    print("2. view tasks")
    print("3. complete task")
    print("4. add note to task")
    print("5. Exit")


def main():
    show_menu()
    while True:
        choice = int(input("Enter your choice (a number 1-5): "))

        if choice == 1:
            new_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            note_task()
        elif choice == 5:
            break
        else:
            print("Invalid Input")


main()

