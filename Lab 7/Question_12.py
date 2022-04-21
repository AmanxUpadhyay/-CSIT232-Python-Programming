# Write a program that gets a string from the user containing a potential telephone number.
# The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise. A phone number is considered valid as long as it is written in the form
# abc-def-hijk or 1-abc-def-hijk.

# The dashes must be included, the phone number should contain only numbers and dashes, and the number of digits in each group must be correct.

def main():
    phone_number = input("Enter a potential phone number: ")
    if phone_number.isdigit() == True:
        print("Invalid")
    elif phone_number.count("-") == 2:
        print("Valid")
    elif phone_number.count("-") == 3:
        print("Valid")
    else:
        print("Invalid")
    
main()