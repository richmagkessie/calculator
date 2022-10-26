# this program encrypts password without any built in python module
def password_encrypt():
    username = input('What\'s your username ')
    password = input('Enter your password ')

    #encrypt password
    password_length = len(password)
    hidden_password = '*' * password_length

    #print message
    print(f'Hello {username}, your password, {hidden_password} is {password_length} characters long ')

#call function
password_encrypt()
