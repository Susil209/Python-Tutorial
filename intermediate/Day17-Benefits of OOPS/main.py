# # Create a class

# class User:
#     # constructor
#     def __init__(self, user_id, first, last, age):
#         self.id = user_id
#         self.first = first
#         self.last = last
#         self.email = first + "." + last + "@company.in"
#         self.age = age
#         self.follower = 0
#         self.following = 0
#
#     def __str__(self):
#         return (f"firstname = {self.first}, lastname = {self.last},"
#                 f"emailId = {self.email}, age = {self.age},"
#                 f"followers = {self.follower}, following = {self.following}")
#
#     # methods
#     def follow(self, user):
#         user.follower += 1
#         self.following += 1
#
#     def getfullname(self):
#         return self.first + " " + self.last
#
#
# # objects
# user1 = User("001", "susil", "nayak", 24)
# user2 = User("002", "akash", "mishra", 28)
#
# user1.follow(user2)
#
# print(user1)
# print(user2)
#
# print(user1.getfullname())
# # or
# # print(User.getfullname(user1))

from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(QuestionModel(item["text"], item["answer"]))

# print(question_bank[0].text)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"Your quiz is completed. Your final score is {quiz.score}/{quiz.question_number}.")
