# Ask the user to enter a sentence and print out the third word of the sentence.
# If the sentence doesn't have at least three words, print out an error message.

Sentence = input("Enter a sentence: ")
Sentence = Sentence.split()
if len(Sentence) >= 3:
    print(Sentence[2])
else:
    print("Error: The sentence doesn't have at least three words.")
    print("Please try again.")
    Sentence = input("Enter a sentence: ")
    Sentence = Sentence.split()
    print(Sentence[2])
    print("Thank you for using the program.")
    print("Goodbye!")

# Ask the user to enter a sentence and print out every third word of the sentence.

Sentence = input("Enter a sentence: ")
Sentence = Sentence.split()
for i in range(0, len(Sentence), 3):
    print(Sentence[i])
print("Thank you for using the program.")
print("Goodbye!")
