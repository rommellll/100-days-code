from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        # Images
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        # Labels
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=2, row=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=1, row=2, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text="t", font=("Arial", 15, "italic"),
                                                     width=200, fill=THEME_COLOR)

        # Buttons
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=1, row=3)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=2, row=3)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            messagebox.showinfo(title="Completed",
                                message=f"You completed the quiz! Your final score is: {self.quiz.score}")

    def answer_true(self):
        answer = "True"
        is_correct = self.quiz.check_answer(answer)
        self.give_feedback(is_correct)

    def answer_false(self):
        answer = "False"
        is_correct = self.quiz.check_answer(answer)
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.next_question)
