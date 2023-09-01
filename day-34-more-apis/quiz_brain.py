import html


class QuizBrain:

    def __init__(self, question_list):
        self.current_question = None
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        question = f"Q.{self.question_number}: {q_text}"
        return question
        # answer = input(f"Q.{self.question_number}: {q_text} (True/False)?: ")
        # self.check_answer(answer, self.current_question.answer)

    def check_answer(self, answer):
        if answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False
