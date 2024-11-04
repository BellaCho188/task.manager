"""
for iteration 3:
1. order date (done!-Avery)
2. then order the time (done!-Bella)
3. edit the task
"""
from operator import itemgetter #will help extract the date, currently doesn't do anything
from flask import Flask
app = Flask(task.man)
task = [] #intitalizing of list

#===============================================================
from datetime import date
from datetime import datetime
#==============================================================
def sort_date(): 
    task.sort(key = lambda x: x[2])#sorts by the submission time
    task.sort(key = lambda x: x[1])#sorts by the date
    for i, j in enumerate(task):#enumerate adds a counter as the key of the object
        print(i + 1, " ", j)

def add_task():
    user_task = input("Enter Your Task>>")
    user_due_date = input("Enter the due date (format: MM-DD-YYY)>>")
    user_due_time = input("Enter the due time (format: HH:MM) >>")
    task.append(((user_task, user_due_date, user_due_time))) #three parenthesis for the 2 things needed to append
    print("Task was successfully added!")



def note_task():
    view_task()
    select_task = int(input("Which task would you like to add a note to? "))
    note_task = str(input("Enter note: "))
    task[select_task-1] = task[select_task-1] +'  NOTE: '+ note_task

def view_task():
    sort_date()


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
            note_task()
        elif choice == 5:
            break
        else:
            print("Invalid Input")


main()