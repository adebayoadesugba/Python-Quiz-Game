from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []




for i in range(len(question_data)):
    n_question = question_data[i]["text"]
    n_answer = question_data[i]["answer"]
    new_q = Question(n_question, n_answer)
    question_bank.append(new_q)
    # print(f"{i}. {question}")
    # print(answer)
    # print(new_q.question)
    # print(new_q.answer)

quiz = QuizBrain(question_bank) 
while quiz.still_more_question():
    quiz.next_question()
    quiz.is_correct()
print("Game Completed 🙏")
print(f"Final Score: {quiz.score}/{len(question_bank)}")