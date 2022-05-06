# Write  program in python to accept the file name from the user and display the contents of the file.
# Use Try and Except block for any error.

FileName = input("Enter a file name: ")
try:
    File = open(FileName, "r")
    try:
        print(File.read())
        File.close()
    except:
        print("Error")
        File.close()
except:
    print("File not found")