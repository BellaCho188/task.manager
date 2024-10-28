from operator import itemgetter #will help extract the date
task = []
from datetime import date
from datetime import datetime
#=====================================================
def sort_date(): 
    #sorted_task = sorted(task,key=itemgetter(1)) # will sort by the second element
    for i, j in enumerate(task):#enumerate adds a counter as the key of the object
        print(i + 1, " ", j)

def add_task():
    user_task = input("Enter Your Task>>")
    user_due_date = input("Enter the due date (format: MM-DD-YYY)>>")
    try: #allows to test a block of code for errors
        #due_date = datetime.strptime(user_due_date, "%m-%d-%Y")
        task.append((user_task, user_due_date))#double parenthesis for the 2 things needed to append
        print("Task was successfully added!")

    except ValueError: #if error occurs, will prompt with:
        print("invalid date format, please use MM-DD-YYY")

def view_task():
    sort_date()


def complete_task():
    task_num = int(input("Enter task that you have completed"))
    task.pop1(task_num - 1)
    view_task()


def show_menu():
    print("Welcome to task management system")
    print("1. Add new task")
    print("2. view task")
    print("3. complete task")
    print("4. Exit")


def main():
    today = date.today()
    
    show_menu()
    while True:
        choice = int(input("Enter Your Choice (as a number)>>"))

        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            break
        else:
            print("Invalid Input")


main()