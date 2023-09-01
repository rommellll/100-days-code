from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from ui import QuizInterface

question_bank = []

for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
# while quiz.still_has_question():
#     quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")