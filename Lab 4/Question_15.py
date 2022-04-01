# Write a program that asks the user for a message and encrypts the message using the one-time pad.

import onetimepad as otp

# Take String from user and convert into Lowercase
message = input('Enter the message: ').lower()

# Take key from user and convert into Lowercase
key = input('Enter the key: ').lower()

# Encrypt the message
encrypted_message = otp.encrypt(message, key)

# Print the encrypted message
print('Encrypted message: ', encrypted_message)

# Decrypt the message
decrypted_message = otp.decrypt(encrypted_message, key)

# Print the decrypted message
print('Decrypted message: ', decrypted_message)