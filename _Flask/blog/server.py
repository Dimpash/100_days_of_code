from flask import Flask, render_template
from post import Post


post = Post()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post.blog_posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    post.get_data(post_id)
    return render_template("post.html", post_data=post.current_post)


if __name__ == "__main__":
    app.run(debug=True)
