print("....................welcome user.....................")
print("Yipee! It is time to roll the dice.")
import random
random_num = random.randint(1, 6)
user_input = str(input("type continue to roll the dice: ")) #user is to type continue
print(random_num) #computer is to print the random_num
user_input = str(input('press continue to roll the dice again or finish to not roll again: ')) #check to see if the user types in continue
if user_input == "finish":
    print("Thank you user. Goodbye.")
else:
    random_num = random.randint(1, 6)
    print(random_num) #computer is to print the random_number


'''
The simulator only takes in the input twice.
Make it run until the user decides to quit.

'''
    
    