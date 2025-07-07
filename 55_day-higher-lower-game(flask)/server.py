import random
from flask import  Flask

random_number = random.randint(0, 9)
print(f"Generated random number: {random_number}")

app = Flask(__name__)

@app.route('/')
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")

@app.route('/<int:user_number>')
def is_number_guessed(user_number):
    print(f"User number: {user_number}")
    # Show a GIF if user_number (an integer) is equal to random_number.
    if user_number == random_number:
        return ("<h1 style='color: purple'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif user_number < random_number:
        return ("<h1 style='color: red'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
    else:
        return ("<h1 style='color: green'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")

if __name__ == "__main__":
    app.run(port=8001, debug=True)



