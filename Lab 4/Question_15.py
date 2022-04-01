# Write a program that asks the user for a message and encrypts the message using the one-time pad.

import onetimepad as otp

# Function to encrypt the message
def encrypt(message, key):
    encrypted_message = otp.encrypt(message, key)
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, key):
    decrypted_message = otp.decrypt(encrypted_message, key)
    return decrypted_message

# Driver code
message = input('Enter the message: ').lower()
key = input('Enter the key: ').lower()

while True:
    print('\n1. Encrypt the message\n2. Decrypt the message\n3. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        encrypted_message = encrypt(message, key)
        print('Encrypted message: ', encrypted_message)
    elif choice == 2:
        decrypted_message = decrypt(message, key)
        print('Decrypted message: ', decrypted_message)
    elif choice == 3:
        break
    else:
        print('Invalid choice')