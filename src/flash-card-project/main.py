from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

right_words = 0
wrong_words = 0

data = pandas.read_csv("data/data.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_background, image=back_img)
    canvas.itemconfig(card_title, text="Russian", fill="white")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="white")


# ---------------------------- CARD VIEWER ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- KNOWN ------------------------------- #
def known():
    global right_words
    right_words += 1
    with open("data/known_words.txt", "a", encoding="utf8") as file_data:
        file_data.write(f"{current_card['English']}: {current_card['Russian']} \n")
    canvas.itemconfig(known_scores, text=right_words)
    next_card()


# ---------------------------- UNKNOWN ------------------------------- #
def unknown():
    global wrong_words
    wrong_words += 1
    with open("data/unknown_words.txt", "a", encoding="utf8") as file_data:
        file_data.write(f"{current_card['English']}: {current_card['Russian']} \n")
    canvas.itemconfig(unknown_scores, text=wrong_words)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
known_words = canvas.create_text(650, 50, text="Known Words", font=("Ariel", 16, "bold"))
unknown_words = canvas.create_text(150, 50, text="Unknown Words", font=("Ariel", 16, "bold"))
known_scores = canvas.create_text(650, 90, text="0", font=("Ariel", 16, "italic"))
unknown_scores = canvas.create_text(150, 90, text="0", font=("Ariel", 16, "italic"))
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=unknown)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=known)
right_btn.grid(column=1, row=1)

next_card()


window.mainloop()
