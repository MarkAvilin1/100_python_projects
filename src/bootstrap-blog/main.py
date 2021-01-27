from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route('/index.html')
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/post.html")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
