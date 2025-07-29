print("Welcome to the Python Quiz Game!")
score = 0

# Questions and answers as a list of dictionaries
questions = [
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyper Text Markup Language", "B. Home Tool Markup Language", "C. Hyperlinks and Text Markup Language"],
        "answer": "A"
    },
    {
        "question": "Which language is used for styling web pages?",
        "options": ["A. HTML", "B. CSS", "C. Python"],
        "answer": "B"
    },
    {
        "question": "Which is the correct syntax to print in Python?",
        "options": ["A. echo 'Hello'", "B. printf('Hello')", "C. print('Hello')"],
        "answer": "C"
    }
]

# Loop through each question
for index, q in enumerate(questions):
    print(f"\nQ{index + 1}: {q['question']}")
    for option in q["options"]:
        print(option)
    
    user_answer = input("Your answer (A/B/C): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}")

# Final Score
print(f"\nYour Final Score: {score} out of {len(questions)}")
