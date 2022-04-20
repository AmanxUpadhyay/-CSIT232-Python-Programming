# Write a simple quote-of-the-day program. The program should contain a list of quotes, and when the user runs the program, a randomly selected quote should be printed.

Quotes = [
    "I'm not a great programmer; I'm just a good programmer with great habits.",
    "Code is not a lie.",
    "Programming is like solving a puzzle, you don't know the answer until you've solved it.",
    "Programming is like building a multilingual"]
import random
print(Quotes[random.randint(0, len(Quotes) - 1)])