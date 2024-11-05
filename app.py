from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST']) #@ decorator modifies functions
def index():
    if request.method != 'POST':
        return render_template('index.html')
    choice = request.form.get("menu", type=int)
    print(choice)
    return render_template('index.html')

@app.route("/goodbye_world")
def goodbye_world():
    return "goodbye world"

if __name__ == "__main__":
    app.run(debug=True)