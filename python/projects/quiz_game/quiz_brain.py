#TODO
#asking the questions
#checking if the answer was correct
#check if we are at the end

class QuizBrain:
    def __init__(self, q_list):
        #default value of 0
        self.question_number = 0
        #create question list from question model
        self.question_list = q_list
        #keep score in check answer method
        self.score = 0

    def still_has_questions(self):
        #if question number is less than the items in question list
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        #current question is the item in self.question_list with the question number like a loop
        current_question = self.question_list[self.question_number]
        #question number cannot be 0
        self.question_number += 1
        #insert current question number & current question text
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        #user answer vs question answer
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("You got it right")
        else:
            print("Wrong answer.")
        print(f"The correct answer was: {correct_answer}")
        #display score out of current question number
        print(f"Your current score is: {self.score}/{self.question_number}\n")




