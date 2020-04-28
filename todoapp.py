from flask import Flask, render_template, request

app = Flask(__name__)


class ToDo:
    task = None
    email = None
    priority = None


todo_list = []


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route("/submit", methods=["POST"])
def submit():
    task = request.form["Task"]
    email = request.form["Email"]
    priority = request.form["Priority Level"]
    newTodo = ToDo()
    newTodo.task = task
    newTodo.email = email
    newTodo.priority = priority
    todo_list.append(newTodo)
    return render_template('index.html', todo_list=todo_list)

@app.route("/clear")
def clear():
    todo_list.clear()
    return render_template('index.html', todo_list=todo_list)


if __name__ == '__main__':
    app.run()
