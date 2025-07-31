import random

subjects = [
           "AI",
           "Machine Learning",
           "Data Science",
           "Cybersecurity",
           "Blockchain", 
           "Quantum Computing",
           "Robotics",
           "Internet of Things",
           "Blockchain",
           "Quantum Computing",
           "Robotics",
           "Internet of Things"
]

actions = [
    "Launched",
    "Developed",
    "Announced",
    "Released",
    "Completed",
    "Achieved",
    "Discovered",
    "Invented",
]

places = [
    "New York",
    "London",
    "Paris",
    "Tokyo",
    "Sydney",
    "Berlin",
    "Rome",
    "Madrid",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    print(f"{action} {subject} in {place}")
    user_input = input("Do you want to generate another news? (y/n): ")
    if user_input.lower() != "y":
        break

print("Thank you for using the Fake News Generator!")