from flask import Flask
import random

rand = random.randint(0, 9)
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media2.giphy.com/media/26DN3US3zaEJ5WZtC/giphy.webp?cid=ecf05e472coxkedv6cz1yu5pgo46' \
           'jwv3yileolrp36tzc90d&rid=giphy.webp">'

@app.route('/<int:num>')
def guess_num(num):
    if num > rand:
        return f'<h1>The number is smaller!</h1>' \
               '<img src="https://media1.giphy.com/media/9u5SmANtz7zIQ/giphy.gif?cid=ecf05e47ta1t4q3oj6f3gfmdppkj44' \
               'kkag38ncxfhb11mboh&rid=giphy.gif">'
    elif num < rand:
        return f'<h1>The number is bigger!</h1>' \
               '<img src="https://media4.giphy.com/media/B2HqyXi7r6j9W9cCG2/giphy.gif?cid=ecf05e47w6658nji03dzb2' \
               'zewilt05r1z2gam6b820jndlqa&rid=giphy.gif">'
    else:
        return f'<h1>You got it! congrats! </h1>' \
               '<img src="https://media2.giphy.com/media/1jWaJ8RgySqOaPjl45/giphy.gif?cid=ecf05e47u7r029jxjcq9k0' \
               'baxnhzphpyl2gfyf7sxg2nr1qa&rid=giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
