"""
for iteration 3:
1. order date (done!-Avery)
2. then order the time (done!-Bella)
3. edit the task (done! -Avery)
4. create flask prototype

to do:
    add am & pm to date
    username and password?
"""
from operator import itemgetter #will help extract the date, currently doesn't do anything
from flask import Flask
app = Flask(__name__)
task = [] #intitalizing of list

#===============================================================
from datetime import date
from datetime import datetime
#==============================================================

class Tasks:
    
    def __init__(self, user_task, due_date, due_time):
        self.user_task = user_task
        self.due_date = due_date
        self.due_time = due_time

    def show_det(self):
        print(f"Task: {self.user_task}, Due Date: {self.due_date}, Time Due: {self.due_time}")
    
    def task_editor(self, edited_task):
        self.user_task = edited_task
        
    def date_editor(self, edited_date):
        self.due_date = edited_date
        
    def time_editor(self, edited_time):
        self.due_time = edited_time


def add_task():
    user_task = input("Enter Your Task>>")
    due_date = input("Enter the due date (format: MM-DD-YYY)>>")
    due_time = input("Enter the due time (format: HH:MM) >>")
    task.append(Tasks(user_task,due_date,due_time)) #three parenthesis for the 3 things needed to append
    print("Task was successfully added!")

def view_task(): 
    print("YOUR TASKS:")
    task.sort(key = lambda x: x.due_time)#sorts by the submission time
    task.sort(key = lambda x: x.due_date)#sorts by the date
    for i, obj in enumerate(task):
        print(i+1," ",f"{obj.user_task}, Due Date: {obj.due_date}, Time Due: {obj.due_time}")

def edit_task():
    view_task()
    select_task = int(input("Which task would you like to edit? "))
    print(" ")
    task[select_task-1].show_det()
    print(" ")
    print("EDITING OPTIONS:")
    print("1. Change name of task")
    print("2. Change due date")
    print("3. Change due time")
    print("4. Exit editor")
    editing = 1
    while editing == 1:
        change = int(input("What do you want to change? "))
        if change == 1:
            edited_task = str(input("Enter edit: "))
            task[select_task-1].task_editor(edited_task)
            print("Changes saved!")
        elif change == 2:
            edited_date = str(input("Enter edit: "))
            task[select_task-1].date_editor(edited_date)
            print("Changes saved!")
        elif change == 3:
            edited_time = str(input("Enter edit: "))
            task[select_task-1].time_editor(edited_time)
            print("Changes saved!")
        elif change == 4:
            editing = 0
        else:
            print("Invalid Input")
        
        
def complete_task():
    view_task()
    task_num = int(input("Enter task that you have completed: "))
    task.pop(task_num - 1)
    view_task()


def show_menu():
    print("These are your options:")
    print(" ")
    print("1. Add new task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Edit task")
    print("5. Exit")


def main():
    
    today = date.today()
    username = input("What is your name? ")
    
    print(" ")
    print("Hi",username,"! Welcome to your task manager!")
    print("Today's date: ", today)
    print(" ")
    show_menu()
    
    while True:
        print(" ")
        choice = int(input("Enter Your Choice (as a number)>>"))
        print(" ")
        
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            edit_task()
        elif choice == 5:
            break
        else:
            print("Invalid Input")


main()