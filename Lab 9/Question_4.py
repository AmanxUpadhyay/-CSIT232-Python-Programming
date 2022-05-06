# Write a program that reads a file and writes out a new file with the lines in reversed order(i.e. the first line in the old file becomes the last one in the new file.)

OldFile = open("STORY.txt", "r")
NewFile = open("STORY_Reversed.txt", "w")
try:
    for Line in OldFile:
        NewFile.write(Line)
    NewFile.close()
    OldFile.close()
except:
    print("Error")
    NewFile.close()
    OldFile.close()