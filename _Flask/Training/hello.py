from flask import Flask


app = Flask(__name__)


# def set_bold(function):
#     # def wrapper_function():
#     #     function
#     # return wrapper_function
#     return f'<b>{function}</b>'
def set_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function


def set_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function


def set_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>" \
           "<p>First paragraph</p>" \
           '<img src="https://media.giphy.com/media/Z8vqwp8LKBouvIIGJX/giphy.gif">' \
           '<p>End</p>'


@app.route("/bye")
@set_bold
@set_emphasis
@set_underlined
def say_bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello dear {name}. Your number is {number}!"


if __name__ == "__main__":
    app.run(debug=True)
