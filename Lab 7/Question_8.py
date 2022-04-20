# Write a program that simulates drawing names out of a hat. In this drawing, the number of hat entries each person gets may vary. Allow the user to input a list of names and a list of how many entries each person has in the drawing, and print out who wins the drawing.

import random

def HatDrawing():
    Names = input("Enter a list of names: ")
    Names = Names.split()
    Entries = input("Enter a list of entries: ")
    Entries = Entries.split()
    Hat = []
    for i in range(len(Names)):
        for j in range(int(Entries[i])):
            Hat.append(Names[i])
    random.shuffle(Hat)
    print(Hat)
    Winner = Hat[0]
    print("The winner is:", Winner)
    print("Thank you for using the program.")
    print("Goodbye!")

HatDrawing()