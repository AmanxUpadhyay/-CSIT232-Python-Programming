# Write a program that reads words.txt and prints only the words with more than 15 characters(not counting white space).

FileName = input("Enter a file name: ")
try:
    File = open(FileName, "r")
    try:
        for Line in File:
            if len(Line) > 15:
                print(Line)
        File.close()
    except:
        print("Error")
        File.close()
except:
    print("File not found")