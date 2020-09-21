


a = ['r', 's', 't', 'a', 'c', 'd', 'r', 's', 't', 'a', 'c', 'd']

b = sorted(a, key = lambda x: 1 if x=='r' else 2 if x=='s' else 3 if x =='m' else 4 if x=='f' else 5 if x == 'd' else 6)
b



##################-------------------------------#######################
#Some Ways to implement a dictionary 
#--------------------------------------------------------#
#this has a bad time complexity
#n*m Where m is the no of unique letters
str1 = 'ddffd'
d = {e:str1.count(e) for e in set(str1)}
d    
'''But that traverses the string 1+n times for each unique character 
    (once to create the set, and once for each unique letter to count the number
    of times it appears. i.e., This has quadratic runtime complexity.). 
    Bad result if you have a lot of unique characters in a long string..'''
#---------------------------------------------------------------#
#this has a good time complxity
dc = {}
for let in 'klaseeeeejf':
  dc[let]=dc.setdefault(let, 0)+1
print(dc)


'''That only traverses the string once no matter how long or how many unique characters.'''
#----------------------------------------------------------------#
##similarly
stre = 'rsmfdrsmfdrsm'
dct= {}
for i in stre:
    dct[i] = dct.get(i, 0)+1
    
dct
dct.values= dct.values - 1
dct
#-------------------------------------------------------#

dct = {}
for let in s:
    dct[let] = dct.setdefault(let,0)+1
    
#-----------------------------------------------------------------#

#using a counter
from collections import defaultdict
str1 = 'kjhskjkjjjk'
count=defaultdict(int)
for c in str1:
    count[c]+=1
count
#--------------------------------------------------------------------#
##Ideal way to do this via using collections.Counter
from collections import Counter
str1 = "aabbaba"
Counter(str1)


#------------------------------------------------------------------------#
#error these  doesnt work
s = 'hkjshfshhkj'
dct = {}
dct = {lete:dct.setdefault(lete, 0)+1 for lete in s}
dct  
    


s = 'vghddglkhhgdjhgh'
dct = {letter:s.count(letter) for letter in s}
dct

#or thiee




#or thi
st = 'hhhhhhhhh'
dct = {}
dct = {let:(dct[let]+ 1 if let in dic else 1) for let in st}
dct


dic= {}
s = 'aaaaljsdkfdlskdljfkdls'
dic = {x: dic.get(x, 0) + 1 for x in s}
dic



dic= {}
s = 'aaaaljsdkfdlskdljfkdls'
dic = {x: dic.get(x, 1) for x in s}
dic
