from random import randint

class PasswordManager(object):
    """
    This function Generates random password 
    and can retrieve generated password based on used key
    """
    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.digits = '0123456789'
        self.symbols = '!#$%&'
        self.dct = {}

    def generate_new_password(self, key, length=6):
        letters_array = list(self.letters)+list(self.digits)+list(self.symbols)
        out = ''.join([letters_array[randint(0,len(letters_array)-1)] for i in range(length)])
        self.dct[key]=out
        return out

    def get_saved_password(self, key):
        if key in self.dct:
            return f'Your Password for {key} is {self.dct[key]}'
        else:
            return "Not Found"



        

        
g = PasswordManager()
print(g.generate_new_password('facebook_password', length=8))
print(g.generate_new_password('gmail', length=52))
print(g.generate_new_password('student portal', 8))
print(g.generate_new_password('Million dollar Saving', 1000))


print(g.get_saved_password('gmail'))
print(g.get_saved_password('facebook_password'))
print(g.get_saved_password('student portal'))
print(g.get_saved_password('Not available'))
print(g.__doc__)

