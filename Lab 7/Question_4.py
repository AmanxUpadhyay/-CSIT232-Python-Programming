# Write a program that asks the user to enter a sentence and then randomly rearranges the words of the sentence. Don’t worry about getting punctuation or capitalization correct.

Sentence = input("Enter a sentence: ")
Sentence = Sentence.split()
import random
random.shuffle(Sentence)
print(Sentence)

# Do the above problem, but now make sure that the sentence starts with a capital, that the original first word is not capitalized if it comes in the middle of the sentence, and that the period is in the right place.

Sentence = input("Enter a sentence: ")
Sentence = Sentence.split()
import random
random.shuffle(Sentence)
print(Sentence)
if Sentence[0][0].isupper():
    print(Sentence[0])
else:
    print(Sentence[0].capitalize())
for i in range(1, len(Sentence)):
    print(Sentence[i])
print(".")
print("Thank you for using the program.")
print("Goodbye!")