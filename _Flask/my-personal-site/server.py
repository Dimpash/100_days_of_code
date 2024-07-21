from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

# html5up.net
@app.route("/my_site")
def my_site():
    return render_template("my_site.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
