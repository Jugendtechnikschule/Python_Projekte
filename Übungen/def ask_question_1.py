def ask_question(question, correct_answer):
    global u_answer
    u_answer = input(question)
    print(u_answer)
    if u_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Wrong! The answer was:", correct_answer)
        return False

questions = [
    ("What is the capital of France? ", "paris"),
    ("What is 5 + 3? ", "8"),
    ("What color is the sky? ", "blue"),
]
score = 0

for question, answer in questions:
    if ask_question(question, answer):
        score += 1

print(f"You got {score} out of {len(questions)}!")

print(u_answer)