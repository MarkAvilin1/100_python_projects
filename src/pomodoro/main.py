from tkinter import *
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#55de9c"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark_counter = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    global reps
    global mark_counter
    reps = 0
    mark_counter = 0
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    turns.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global mark_counter
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
        mark_counter = 0
        turns.config(text="")
    elif reps % 2 == 0:
        signs = "✔" * mark_counter
        turns.config(text=signs)
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        mark_counter += 1
        count_down(work_sec)
        title.config(text="Work ", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        playsound('sound.mp3')
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 70, "bold"))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(105, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", bg="#FFFFFF", font=(FONT_NAME, 16, "bold"), command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", bg="#FFFFFF", font=(FONT_NAME, 16, "bold"), command=reset, highlightthickness=0)
reset_btn.grid(column=2, row=2)

turns = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"))
turns.grid(column=1, row=3)

window.mainloop()
