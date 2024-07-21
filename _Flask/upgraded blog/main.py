from flask import Flask, render_template, request
from posts import Posts
from email_sending import send_by_dest_list


# posts = BlogPosts()
posts = Posts()

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("index.html", blog_posts=posts.blog_posts)


@app.route("/index")
def get_index():
    return render_template("index.html", blog_posts=posts.blog_posts)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def get_contact():
    if request.method == 'POST':
        email_text = f" Name: {request.form['name']}\n Email: {request.form['email']}\n Phone:{request.form['phone']}\n Message:{request.form['message']}"
        print(email_text)
        send_by_dest_list(subject='A message from Contact form', email_text=email_text)
        h1_message = True
    else:
        h1_message = False
    return render_template("contact.html", h1_message=h1_message)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    posts.get_data(post_id)
    # print(posts.current_post)
    return render_template("post.html", post_data=posts.current_post)


# @app.route("/form-entry", methods=['POST'])
# def receive_data():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     print(f"name: {name}\n email: {email}\n phone:{phone}\n message:{message}")
#     return f"<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
