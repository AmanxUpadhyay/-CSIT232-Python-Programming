# Write a program that asks the user to enter a length in feet.

# Function to convert feet to inches
def feet_to_inches(feet):
    return feet * 12

# Function to convert feet to yards
def feet_to_yards(feet):
    return feet / 3

# Function to convert feet to miles
def feet_to_miles(feet):
    return feet / 5280

# Function to convert feet to millimeters
def feet_to_millimeters(feet):
    return feet * 304.8

# Function to convert feet to centimeters
def feet_to_centimeters(feet):
    return feet * 30.48

# Function to convert feet to meters
def feet_to_meters(feet):
    return feet * 0.3048

# Function to convert feet to kilometers
def feet_to_kilometers(feet):
    return feet / 3280.84

# Function: Menu
def menu():
    List = ['1. Feet to Inches', '2. Feet to Yards', '3. Feet to Miles', '4. Feet to Millimeters', '5. Feet to Centimeters', '6. Feet to Meters', '7. Feet to Kilometers', '8. Exit']

    print('\n')
    for i in range(len(List)):
        print(List[i])

    choice = int(input('Enter your choice: '))
    while choice < 1 or choice > 8:
        print('Invalid choice. Please try again.')
        choice = int(input('Enter your choice: '))
    return choice

# Driver Code
choice = menu()
while choice != 8:
    if choice == 1:
        feet = float(input('Enter the length in feet: '))
        print('The length in inches is: ', feet_to_inches(feet))
    elif choice == 2:
        feet = float(input('Enter the length in feet: '))
        print('The length in yards is: ', feet_to_yards(feet))
    elif choice == 3:
        feet = float(input('Enter the length in feet: '))
        print('The length in miles is: ', feet_to_miles(feet))
    elif choice == 4:
        feet = float(input('Enter the length in feet: '))
        print('The length in millimeters is: ', feet_to_millimeters(feet))
    elif choice == 5:
        feet = float(input('Enter the length in feet: '))
        print('The length in centimeters is: ', feet_to_centimeters(feet))
    elif choice == 6:
        feet = float(input('Enter the length in feet: '))
        print('The length in meters is: ', feet_to_meters(feet))
    elif choice == 7:
        feet = float(input('Enter the length in feet: '))
        print('The length in kilometers is: ', feet_to_kilometers(feet))
    choice = menu()
print('Thank you for using this program.')