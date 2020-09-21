def password_generator(num_of_letters):
    ''' Generates password based on desired password lenght inputed'''
    import string, random
    data = list(string.ascii_letters)+list(string.digits)
    password = random.choices(data, k =num_of_letters)
    return ''.join(password)

print(password_generator(20))