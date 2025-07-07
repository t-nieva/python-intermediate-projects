from curses import wrapper

from flask import Flask

app = Flask(__name__)

# Decorators
def make_bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper

def make_emphasis(func):
    def wrapper():
        return f'<i>{func()}</i>'
    return wrapper

def make_underlined(func):
    def wrapper():
        return f'<u>{func()}</u>'
    return wrapper

@app.route('/')
def home():
    return ('<h1 style="text-align: center">Привіт, Flask!</h1>'
            '<p>This is paragraph.</p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGdscDR0a3c1Y29pamh3c3RmdjVveHMzNnA5c28wam41YmhzYXQ3ZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/vFKqnCdLPNOKc/giphy.gif" width=200>')

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route('/username/<name>')
def greet(name):
    return f"Hello, {name}."

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
