# Write a python program to merge the content of two files in a third file. the user will provide the filenames.
# Use Try and Except block for any error.

First_FileName = input("Enter the first file name: ")
Second_FileName = input("Enter the second file name: ")
Third_FileName = input("Enter the third file name: ")
try:
    First_File = open(First_FileName, "r")
    Second_File = open(Second_FileName, "r")
    Third_File = open(Third_FileName, "w")
    try:
        Third_File.write(First_File.read())
        Third_File.write(Second_File.read())
        Third_File.close()
        First_File.close()
        Second_File.close()
    except:
        print("Error")
        Third_File.close()
        First_File.close()
        Second_File.close()
except:
    print("File not found")