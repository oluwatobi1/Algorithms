# Goalis to shuffle any sentence inputed by the user
# Allow input
# create a shuffle of inputed sentence 
# display shuffled sentence

from random import shuffle
user_sentence = input("What sentence would you like to shuffle?  ")

sentence = user_sentence.split()
shuffle(sentence)
print("Here's your shuffled sentence:\n ", " ".join(sentence))