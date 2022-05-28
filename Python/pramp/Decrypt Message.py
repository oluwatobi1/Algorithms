# Convert every letter to its ASCII value. Add 1 to the first letter, and then for 
# every letter from the second one to the last one, add the value of the previous letter.
#  Subtract 26 from every letter until it is in the range of lowercase letters a-z in 
# ASCII. Convert the values back to letters.

# For instance, to encrypt the word “crime”

# Decrypted message:	c	r	i	m	e
# Step 1:	99	114	105	109	101
# Step 2:	100	214	319	428	529
# Step 3:	100	110	111	116	113
# Encrypted message:	d	n	o	t	q
# The FBI needs an efficient method to decrypt messages. Write a function 
# named decrypt(word) that receives a string that consists of small latin letters only, 
# and returns the decrypted word.


def decrypt(word):
  # 97-122
  # [int of ascii value]
  # ord(a)=97
  out = ''
  
  ascii_values = []
  for i in word:
    ascii_values.append(ord(i))
  prev = 1
  temp = 0
  for i in range(len(ascii_values)):
    temp = ascii_values[i]
    ascii_values[i]-=prev
    while ascii_values[i]<97:
      ascii_values[i]+=26
    prev = temp
    out+=chr(ascii_values[i])
  return out


print(decrypt('dnotq'))
