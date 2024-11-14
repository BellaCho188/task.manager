from flask import Flask, render_template, request, url_for
import datetime as dt

# flask is the main class used to create the web application
# render_template     renders an html template and passes the data to it
# request             used to handle incoming HTTP requests and form data
# url_for             used to generate url

app = Flask(__name__)  # creates an instance of the flask class


class Task:
    """class for tasks"""

    def __init__(self, user_task: str, due_date: str, due_time: str):
        self.user_task = user_task
        self.due_date = due_date  # dt.date.fromisoformat(due_time)
        self.due_time = due_time  # dt.datetime.strptime("%H:%M")

    def __str__(self) -> str:
        return f"Task: {self.user_task}, Due Date: {self.due_date}, Time Due: {self.due_time}"  # send this information to the html file


tasks: list[Task] = [] # initialize list that holds tasks


# methods specifies the allowed ways the users are allowed to interact with the server
# ['GET']         default its method 
# ['POST']        lets users send html data to server
@app.route("/", methods=["GET", "POST"])  # @ decorator modifies functions
def index():
    if request.method != "POST":
        return render_template(
            "index.html", tasks=tasks
        )  # passes the tasks list to webpage
    if "remove_task" in request.form and tasks:
        tasks.pop(
            request.form.get("index_to_pop", type=int) - 1
        )  # from html file remove task *enumerates the task (starts at 1)
        return render_template("index.html", tasks=tasks)
    if "add_task" in request.form:
        task = Task(
            **{key: val for key, val in request.form.items() if key != "add_task"}
        )
        # creates a new task object by unpacking the form data and passing the arguments to the task constructor
        tasks.append(task)

    sorted_tasks = sorted(
        tasks,
        key=lambda task: (
            dt.datetime.strptime(task.due_date, "%Y-%m-%d"),  # First: sort by due_date
            dt.datetime.strptime(task.due_time, "%H:%M"),  # Second: sort by due_time
        ),  # this strips the string and sorts the dates and times
    )

    return render_template(
        "index.html", tasks=sorted_tasks
    )  # page is updated with new information


if __name__ == "__main__":
    app.run(debug=True)
