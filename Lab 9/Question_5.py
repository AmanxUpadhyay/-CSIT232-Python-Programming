# Write a program that reads a file and prints only those lines that contain the specific substring as provided by the user.

Filename = input("Enter a file name: ")
Substring = input("Enter a substring: ")
try:
    File = open(Filename, "r")
    try:
        for Line in File:
            if Substring in Line:
                print(Line)
        File.close()
    except:
        print("Error")
        File.close()
except:
    print("File not found")