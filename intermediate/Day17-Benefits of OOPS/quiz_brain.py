class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    # method
    def next_question(self):
        question_item = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_item.text} (True/False)?: ")
        self.check_answer(user_answer, question_item.answer)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("That's correct")
            self.score += 1
        else:
            print("No, it's wrong.")
            print(f"The answer is {answer}")
        print(f"Your score is: {self.score}/{self.question_number}")
        print("\n")