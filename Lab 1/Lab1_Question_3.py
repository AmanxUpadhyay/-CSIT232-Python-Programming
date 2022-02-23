# Author: Aman Upadhyay

# Write a python script to read age of a person from keyboard and display whether he/she is eligible for voting or not (age>=18 is eligible for voting).

def VotingEligibility(age):
    if age >= 18:
        print("You are eligible for voting.")
    else:
        print("You are not eligible for voting.")

# Driver Code
age = int(input("Enter your age: "))
VotingEligibility(age)