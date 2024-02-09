from question_model import Question
#from QuestionGameData import question_data
from quiz_brain import QuizBrain
import requests

api_url = "https://opentdb.com/api.php?amount=<amount>&category=<category>&difficulty=<difficulty>&type=boolean"

no_of_questions = int(input("How many questions would you like to use for playing the game?: "))
api_url = api_url.replace("<amount>",str(no_of_questions))
category = int(input("Pick a number between 9-32 to select the category: "))
api_url = api_url.replace("<category>",str(category))
difficulty = input("Pick a difficulty (any/easy/medium/hard): ")
api_url = api_url.replace("<difficulty>",difficulty)

response = requests.get(api_url)
trivia_data = response.json()["results"]

question_bank = []
if len(trivia_data)>0:
    for question in trivia_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_question():
        quiz.next_question()
    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
else:
    print("No questions could be retrieved using TRIVIA database API")



