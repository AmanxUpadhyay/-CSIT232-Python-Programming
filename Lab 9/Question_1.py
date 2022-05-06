# Write a program in python to accept few lines of texts and store in a file Name Story.txt
# Using Try and except block

Sentence = input("Enter a sentence: ")
try:
    File = open("STORY.txt", "w")
    try:
        File.write(Sentence)
        File.close()
    except:
        print("Error")
        File.close()
except:
    print("File not found")