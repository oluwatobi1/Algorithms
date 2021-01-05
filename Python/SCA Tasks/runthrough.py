from random import randint
class PasswordManager:

    def __init__(self):
        #initialize all you instance attributes
        self.character = ''
        self.dictionary= {}

    def generate_new_password(self, key, length=6):        
        password = ''
        for i in range(length):
            rand_index = randint(0, len(self.character))
            password+=self.character[rand_index]
        #store the password here
        self.dictionary[key]=password
        return password

        #logic to generate random password

    def get_saved_password(self, key):
        if key in self.dictionary:
            return f" Your password for {key} is {self.dictionary[key]}"

        else:
            return " Not Found"

g= PasswordManager()
print(g.generate_new_password('facebook', 6))
print(g.get_saved_password('facebook'))



        