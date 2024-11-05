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


@app.route('/',methods = ['GET', 'POST']) #@ decorator modifies functions
def index():
    if request.method != 'POST':
        return render_template('index.html', tasks=tasks)
    form = request.form.to_dict()
    if "remove_task" in request.form and tasks:
        tasks.pop(request.form.get("index_to_pop", type=int) - 1)
        return render_template('index.html', tasks=tasks)   
    if form.pop("add_task") is not None:
        tasks.append(Task(**form))
    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)