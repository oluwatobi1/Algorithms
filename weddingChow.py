def wedding_chow(s):
    """
    Given a string r,s,m,f and d (representing rice, stew, meat, fish and drink respectively)
    This function takes it as input and RETURNS a tuple of two elements.
    The first element is an integer representing the maximum number of guests that can receive complete chow
    and the second is the left over chow as a string arranged in order (rsmfd)
    
    Steps
    1. Store all the chow(letter) and their occurence in a dict
    2. Get the possible number of 'complete chow'
    3. Concatenate letter that occurs more than the possible comp chow( as Overflow)
    4. Sort the overflow into the required format
    5. Return a tuple of 'complete chow' and 'sorted Overflow"
    
    """
    #egde cases check
    if type(s)!= str or len(s)<1:
        return 'Enter a string of chows (rsmfd) only'
    for i in s:
        if i not in 'rsmfd':
            return 'Invalid food type detected'
    
    
    dct = {}
    for let in s:
        dct[let] = dct.setdefault(let,0)+1
        
    complete_chow = min(dct.values()) if len(set(s)) == 5 else 0
    ls = ''
    for i, j in dct.items():
        rem = j-complete_chow
        if rem !=0:
            ls=ls + i*rem
            
    srt = ''.join(sorted(ls, key = lambda x: 1 if x=='r' else 2 if x=='s' else 3
            if x =='m' else 4 if x=='f' else 5 if x == 'd' else 6))
    
    
    return (complete_chow, srt)



            
print(wedding_chow('rsmfdsfrrsmfdrsmfmrsmdsmfd'))


## question 5/5/2020 day 5
'''
WEDDING CHOW
At the reception of GeekTutor's wedding, guests are to be served. A complete chow has rice(r), stew(s), meat(m), fish(f) and a drink(d).

Given a string representing the supplies(chow) available, write a function named wedding_chow() that takes it as input and RETURNS a tuple of two elements.

The first element is an integer representing the maximum number of guests that can receive complete chow

and the second is the left over chow as a string arranged in order (rsmfd)

r,s,m,f and d represent rice, stew, meat, fish and drink respectively.

 

Examples:

wedding_chow(‘rsmfdrsmfdrsm’) will return (2,'rsm') as it has just 2 complete chows.

 

wedding_chow(‘fdrsmssrrdr’) will return (1, 'rrrssd') as there is only one complete chow.

 

*N/B:*
•The strings will not be given in any particular order.

 •No inbuilt modules are allowed.

•Note the case.

•The left over chow should be arranged in order (r,s,m,f,d)

•Only AssertionErrors should be raised.
'''