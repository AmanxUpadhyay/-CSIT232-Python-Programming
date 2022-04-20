# Write a censoring program. Allow the user to enter some text and your program should print out the text with all the curse words starred out.
# The number of stars should match the length of the curse word.
# For the purposes of this program, just use the“curse” words darn, dang, freakin, heck, and shoot.

def Censoring():
    Text = input("Enter some text: ")
    Text = Text.split()
    Curse = ["darn", "dang", "freakin", "heck", "shoot"]
    for i in range(len(Text)):
        if Text[i] in Curse:
            print("*" * len(Text[i]))
        else:
            print(Text[i])
    print("Thank you for using the program.")

Censoring()