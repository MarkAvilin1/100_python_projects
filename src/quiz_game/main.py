from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [i for i in [Question(q["text"], q["answer"]) for q in question_data]]

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print()
    if quiz.question_number == len(quiz.question_list):
        print("You've completed the quiz!")
        if quiz.score > (quiz.question_number / 2):
            print("You are won! Congrats! :D")
        else:
            print("Yoe are lost! Sorry!!!")
        print(f"You've scored: {quiz.score}/{quiz.question_number}!")
