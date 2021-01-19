from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, command=self.it_is_true)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, command=self.it_is_false)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            if self.quiz.score >= 5:
                self.canvas.itemconfig(self.question_text, text="You Won! Congrats!\nYou've reached the end of the "
                                                                f"quiz, you've got ({self.quiz.score} of 10)")
            else:
                self.canvas.itemconfig(self.question_text, text="You lost! Hard luck!\nYou've reached the end of the "
                                                                f"quiz, you've got ({self.quiz.score} of 10)")
            self.true_btn.config(state="disable")
            self.false_btn.config(state="disable")

    def it_is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def it_is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)
