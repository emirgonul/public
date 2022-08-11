from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#build a new question bank list of question objects
question_bank = []
#loop through question data list to get dict items and seperate them 
#question = {"text": "A slug's blood is green.", "answer": "True"},
for question in question_data:
    #get text and answer key's value
    q_text = question['question']
    q_answer = question['correct_answer']
    #construct new question with passing data from list of dicts
    new_question = Question(q_text, q_answer)
    #pass questions to new_question list
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
#if the quiz still has questions remaining 
while QuizBrain.still_has_questions:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")