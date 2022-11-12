from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=340, height=470, bg=THEME_COLOR, padx=20, pady=20)

        self.lbl_score = Label(text="Score: 0/0", font=(FONT_NAME, 15, ""), bg=THEME_COLOR, fg="white")
        self.lbl_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Here has to be the quiz text.",
            font=(FONT_NAME, 20, "italic"),
            fill="black",
            width=300
            )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images\\true.png")
        self.btn_true = Button(image=true_img, bd=0, highlightthickness=0, command=self.click_true)
        self.btn_true.grid(column=0, row=2)
        self.btn_true.config()

        false_img = PhotoImage(file="images\\false.png")
        self.btn_false = Button(image=false_img, bd=0, highlightthickness=0, command=self.click_false)
        self.btn_false.grid(column=1, row=2)
        self.btn_false.config()

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.lbl_score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:

            self.canvas.itemconfig(self.question_text,
                                   text=f"Final. The score is: {self.quiz.score}/{self.quiz.question_number}")
            self.btn_true.config(state="disable")
            self.btn_false.config(state="disable")


    def click_true(self):
        self.give_feedback(bool(self.quiz.check_answer("True")))

    def click_false(self):
        self.give_feedback(bool(self.quiz.check_answer("False")))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

