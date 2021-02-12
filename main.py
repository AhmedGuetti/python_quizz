from questions import question
file = open("questions.txt", "r")
question_prompt = file.readlines()

#Answer goes here
questions = [
    question(question_prompt[0], "b"),
    question(question_prompt[1], "a"),
    question(question_prompt[2], "c")
]


for question in questions:
    score = 0
    answer = input(question.prompt)
    if question.answer == answer:
        score += 1
    else:
        continue
print("Your score is :" + str(score) + "/" + str(len(questions)))




file.close()