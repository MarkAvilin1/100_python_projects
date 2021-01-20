from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def inner_func():
        "<b>"
        func()
        "</b>"

    return inner_func()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
def say_bye():
    return 'good bye!'


@app.route('/<name>')
def greet(name):
    return f"Hello there {name}!"


@app.route('/<name>/<int:number>')
def name_age(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == '__main__':
    app.run(debug=True)
