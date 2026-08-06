questions = ("Which continent is Russia in?: ",
             "What is 778 + 789?:",
              "How much DNA do humans share with bananas?:",
               "What is the rarest naturally occuring element on Earth's crust?:",
                "What is the chemical symbol for salt?:" )
options = (("A.Antartica","B.Europe","C.Asia","D.B and C")
           ("A.1567","B.1557","C.1568","D.1566")
           ("A.50%","B.60%","C.70%","D.80%")
           ("A.Astatine","B.Francium","C.Rhodium","D.Tellurium")
           ("A.NaCl","B.H2O","C.CO2","D.O2"))
answers = ("D","A","C","C","A")
guesses = []
score = 0 
question_num = 0
score = 0
guesses = []

for i in range(len(questions)):

    print("""
""" + questions[i])
    for option in options[i]:
        print(option)
    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    
    if guess == answers[i]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {answers[i]}.")

# Display total score

print(f"You got {score} out of {len(questions)} correct.")
percentage = (score / len(questions)) * 100
print(f"Your score percentage is: {percentage}%")
import random

question_order = list(range(len(questions)))
random.shuffle(question_order)
def run_quiz(questions, options, answers):
    score = 0
    guesses = []
    for i in range(len(questions)):
        print("" + questions[i])

        for option in options[i]:
            print(option)
        guess = input("Enter your answer (A, B, C, or D): ").upper()
        guesses.append(guess)
        if guess == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {answers[i]}")

print(f"Final score: {score} / {len(questions)}")
print(f"Percentage: {(score/len(questions))*100%")
