from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    date = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=date)

@app.route('/guess/<name>')
def guess(name):
    gender_api = requests.get(f"https://api.genderize.io?name={name}")
    age_api = requests.get(f"https://api.agify.io?name={name}")
    gender = gender_api.json()["gender"]
    age = age_api.json()["age"]
    return render_template("guess.html", username=name, gender=gender, age=age)


if __name__ == '__main__':
    app.run(debug=True)
