class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, current_question_answer):
        if answer.lower() == current_question_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {current_question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
