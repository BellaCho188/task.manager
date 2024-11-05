from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


class Task:
    """class for tasks"""

    def __init__(self, user_task: str, due_date: str, due_time: str):
        self.user_task = user_task
        self.due_date = due_date
        self.due_time = due_time

    def __str__(self) -> str:
        return f"Task: {self.user_task}, Due Date: {self.due_date}, Time Due: {self.due_time}"


tasks: list[Task] = []


# methods specifies the allowed ways the users are allowed to interact with the server
# defualt its method = ['GET']
@app.route("/", methods=["GET", "POST"])  # @ decorator modifies functions
def index():
    if request.method != "POST":
        return render_template("index.html", tasks=tasks)
    if "remove_task" in request.form and tasks:
        tasks.pop(
            request.form.get("index_to_pop", type=int) - 1
        )  # from html file remove task *enumerates the task (starts at 1)
        return render_template("index.html", tasks=tasks)
    if "add_task" in request.form:
        task = Task(
            **{key: val for key, val in request.form.items() if key != "add_task"}
        )
        # dictionary unpacking, k, v creates a new dictionary and removes adds task
        # ** unpacks the dictionary Task(**{due_date="2024"}) == Task(due_date="2024")
        tasks.append(task)
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)
