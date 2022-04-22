# Dictionaries provide a convenient way to store structured data. Here is an example dictionary:
# d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
# {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
# {'name':'Princess', 'phone':'555-3141', 'email':''},
# {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

# Write a program that reads through any dictionary like this and prints the following:
# (a) All the users whose phone number ends in an 8
# (b) All the users that don’t have an email address listed

def main():
    d=[{'name':'Todd', 'phone':'555-1414', 'email':' '},
    {'name':'Helga', 'phone':'555-1618', 'email':' '},
    {'name':'Princess', 'phone':'555-3141', 'email':' '},
    {'name':'LJ', 'phone':'555-2718', 'email':' '}]
    for user in d:
        if user['phone'][-1] == '8':
            print(user['name'])
    for user in d:
        if user['email'] == ' ':
            print(user['name'])
        
main()