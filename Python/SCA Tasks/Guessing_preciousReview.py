print("Welcome User.................................................")
print("This is a guessing game where you pick a number at random")
import random 

random_number = random.randint(0, 19) #save the random number to a variable
print("hint: number is between 0 and 19") #hint for the user
user_input = int(input("type in your guess: ")) #the user is to guess the number
# check the value to see if it is the number
if random_number > user_input:
    print("Your guess is lesser and you have four more tries")
elif random_number < user_input:
    print("your guess is greater and you have four more tries")
else:
    print("your guess is correct")
import random
random_number = random.randint(2, 18) #save the random number to a variable
print("hint: number can be a multiple of twos or three but must not exceed 18") #hint for the user
user_input = int(input("type in your guess: ")) #the user is to guess the number
# check the value to see if it is the number
if random_number > user_input:
    print("your guess is lesser and you have three more tries")
elif random_number < user_input:
    print("your guess is greater and you have three more tries")
else: 
    print("Your guess is correct")
import random
random_number = random.randint(1, 20) #save the random number to a variable
print("hint: number can be even or odd")
user_input = int(input("type in your guess: ")) #the user is to guess the number
#check the value to see if it is correct
if random_number == user_input:
    print("Your guess is correct")
elif random_number > user_input:
    print("your guess is lesser and you have two more tries")
else:
    print("your guess is greater and you have two more tries")
import random
random_number = random.randint(0, 19) #save the random number to a variable
print("hint: use the first hint")
user__input = int(input("type in your guess: ")) #the user is to guess the number
#check the value to see if it is correct
if random_number == user_input:
    print ('your guess is correct')
elif random_number > user_input:
    print("your guess is lesser and you have one more try left")
else:
    print("your guess is greater and you have one more try left")
import random 
random_number = random.randint(2, 18) # save the random number to a variable 
print("hint: number must not be lesser than 2")
user_input = int(input("type in your guess: ")) #the user is to guess the number
#check the value to see if it is correct
if random_number == user_input:
    print("your guess is correct")
elif random_number > user_input:
    print("your guess is lesser\n Game over")
else:
    print("your guess is greater\n Game over")
    

'''
Code is too verbose(Not following the DRY Principle) needs refactoring.
 Not user friendly. (you need to out the answer at the end)
 The hints are not very helpful.

 the very difficult for a user to get the answer.

'''