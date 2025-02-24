import html

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        current_question_text = html.unescape(self.current_question.text)
        # current_question_answer = current_question.answer
        self.question_number += 1
        print(current_question_text, self.current_question.answer)
        return f"Q.{self.question_number}: {current_question_text}(True/False)?: "

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
            return True
        else:
            print("That's wrong.")
            return False
