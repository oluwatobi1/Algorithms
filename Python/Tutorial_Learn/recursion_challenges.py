def rec_sum(num):

    '''
    A function that takes an integer and computes the cummulative sum from that
    integer to zero
    for example n = 4  returns 4+3+2+1+0
    '''

    if num ==0:
        return 0
    else:
        return num+rec_sum(num-1)


def sum_func(num):
    """
    returns the sum of the individual digits in the integer 
    usi
    """
    if num//10 ==0:
        return num
    else:
        return num%10+sum_func(num//10)

# print(sum_func(453))    

def word_split(phrase, lst, curr = None, out=None):

    """
    this function takes in a string phrase and a set of words and 
    determines if it is possible to split the string in  a way  in 
    which the words can be made from the list of words..

    eg 
    word_split('themanran', ['the', 'man', 'ran']) --> ['the', 'man', 'ran']
    word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'loves', 'John'])-->['i', 'love', 'dogs', 'John']
    word_split('themanran', ['clown', 'man', 'ran']) --> []


    """

    if not out:
        out = []

    if not curr:
        curr = 0
    if len(phrase)<=0 or curr>len(phrase):
        return out

    if phrase[:curr] in lst:
        out.append(phrase[:curr])
        phrase = phrase[curr:]
        # print(phrase, 'outere ', out)
        return word_split(phrase, lst, curr, out)
    else:
        # print(phrase, 'secon ', out, "or e", phrase[:curr])
        return word_split(phrase, lst, curr+1, out)

phrase = 'ilovedogsJohn'
lst = ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']
print(word_split('themanran', ['clown', 'man', 'ran']))
