# Author: Aman Upadhyay

# Write a python script to check the given year is leap year or not.

def LeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Driver Code
year = int(input("Enter year: "))
if LeapYear(year):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
