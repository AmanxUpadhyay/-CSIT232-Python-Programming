# Author: Aman Upadhyay

# Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and ask for the number of hours to wait. Your program should output what the time will be on the clock when the alarm goes off.

CurrentTime = int(input("Enter current time: "))
AlarmTime = int(input("Waiting time? "))
Result = (CurrentTime + AlarmTime) % 24
print("The alarm will go off at", Result, ":00")

