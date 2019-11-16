from question import question

question_prompts = [
    "Who is the queen of pop?\n(a) Taylor\n(b) Katy\n(c) Ariana\n\n",
    "Who is the king of pop?\n(a) Michael\n(b) Justin\n(c) Zayn\n\n",
    "Who is the best footballer?\n(a) Cristiano\n\(b) Messi\n(c) Neymar\n\n"
]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "a"),
    question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)