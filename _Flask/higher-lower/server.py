from flask import Flask
from random import randint


# pc_number = randint(0, 9)
pc_number = 0

app = Flask(__name__)


@app.route("/")
def start():
    global pc_number
    pc_number = randint(0, 9)
    print(pc_number)
    return "<h1>Guess a number between 0 and 9</h1>" \
           '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/200w.webp">'

@app.route("/<int:number>")
def check_number(number):
    print(pc_number)
    if number > pc_number:
        result = '<h1 style="color:red;">Too high! Try again.</h1>' \
                 '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < pc_number:
        result = '<h1 style="color:blue;">Too low! Try again.</h1>' \
                 '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        result = '<h1 style="color:green;">Congratulations! You won!</h1>' \
                 '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return result


if __name__ == "__main__":
    app.run(debug=True)