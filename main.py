"""
1. initialize tasks
2. add tasks
3. remove tasks
4. sort tasks
5. display tasks
"""


from datetime import date #import datetime library

task = [] #intitalizing of list

#===============================================================

class Tasks:
    
    def __init__(self, user_task, due_date, due_time): #initialize task attributes
        self.user_task = user_task
        self.due_date = due_date
        self.due_time = due_time

    def show_det(self):
        print(f"Task: {self.user_task}, Due Date: {self.due_date}, Time Due: {self.due_time}")
    

def add_task():
    user_task = input("Enter Your Task>>")
    due_date = input("Enter the due date (format: MM-DD-YYY)>>")
    due_time = input("Enter the due time (format: HH:MM) >>")
    task.append(Tasks(user_task,due_date,due_time))
    print("Task was successfully added!")


def view_task(): 
    print("YOUR TASKS:")
    task.sort(key = lambda x: x.due_time)#sorts by the submission time
    task.sort(key = lambda x: x.due_date)#sorts by the date
    for i, obj in enumerate(task): #number tasks
        print(i+1," ",f"{obj.user_task}, Due Date: {obj.due_date}, Time Due: {obj.due_time}")
        

def complete_task():
    view_task()
    task_num = int(input("Enter task that you have completed: "))
    task.pop(task_num - 1) #remove specified task from list 
    view_task()


def show_menu():
    print("These are your options:")
    print(" ")
    print("1. Add new task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Exit")


def main():
    
    today = date.today()
    
    print(" ")
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
            break
        else:
            print("Invalid Input")


main()