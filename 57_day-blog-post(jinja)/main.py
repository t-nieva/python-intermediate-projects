import requests
from flask import Flask, render_template
from post import Post

post_objects = []
try:
    posts = requests.get("https://api.npoint.io/e7d08518e704a0eac93c").json()
    for post in posts:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)
except Exception as e:
    print(f"Error getting posts: {e}")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == blog_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=8005)
