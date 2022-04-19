# Write a program that asks the user to enter some test and then counts how many articles are in the text. Articles are the words 'a', 'an', 'the'.
# The program should then print the number of articles.

def main():
    text = input("Enter some text: ")
    count = 0
    for word in text.split():
        if word.lower() in ['a', 'an', 'the']:
            count += 1
    print("There are", count, "articles in the text.")

# Call the main function
main()