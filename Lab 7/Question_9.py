# Write a simple quiz game that has a list of ten questions and a list of answers to those questions. The game should give the player four randomly selected questions to answer. It should ask the questions one-by-one, and tell the player whether they got the question right or wrong. At the end it should print out how many out of four they got right.

import random

def Quiz():
    Questions = [
        "What is the capital of California?",
        "What is the capital of Texas?",
        "What is the capital of New York?",
        "What is the capital of Florida?",
        "What is the capital of Pennsylvania?",
        "What is the capital of Illinois?",
        "What is the capital of New Jersey?",
        "What is the capital of New Mexico?",
        "What is the capital of Nevada?"]
    Answers = [
        "Sacramento",
        "Austin",
        "Albany",
        "Tallahassee",
        "Harrisburg",
        "Springfield",
        "Trenton",
        "Santa Fe",
        "Carson City",
        "Reno"]
    Score = 0
    for i in range(4):
        Question = Questions[random.randint(0, len(Questions) - 1)]
        Answer = Answers[random.randint(0, len(Answers) - 1)]
        print("Question", i + 1, ":", Question)
        Guess = input("Your answer: ")
        if Guess == Answer:
            print("Correct!")
            Score += 1
        else:
            print("Incorrect!")
    print("You got", Score, "out of 4 correct.")
    print("Thank you for using the program.")

Quiz()