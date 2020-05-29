def resolve(data, ls):  
    """NOTE:I used RECURSION approach to solve both challenge

    Return a list of the resolved tokens in the same order.

    Args:
        data(dict): dictionary containing token to token 
        ls(list):list of tokens (strings, integers or a combination)
        
    Attributes:
        out_ls(list): an instance of the output array,
        empty(list): A list use to check for connected token in cyclic pattern (to prevent infinite running in circles)

    Function:
        recursion: used to breakdown the implementation of the recursion process
    
       """        
    out_ls = []
    empty = []
    
    for keys in data.keys():
        
        if type(keys) == int and int(keys)<0 :
                raise AssertionError('Enter positive integers')
        elif type(keys) == int and int(keys)>0:
            break
        else:
            try:            
                keys.isalpha() 
            except Exception as exc:
                raise AssertionError('Key is not an alphabet') from exc

    
    for i in ls:
        recursion(data, i, out_ls, empty)
        
    return out_ls
    
#my helper recursion function for the resolve function
def recursion(data, item, out_ls, empty):
    """
    Gets the last appropraite value for an input token.

    Args: 
        data(dict): dictionary containing token to token. 
        item(str):this is an element from the list of tokens (strings, integers or a combination)

        out_ls(list): an instance of the output array
      
        empty(list): A list use to check for connected token in cyclic pattern (to prevent infinite running in circles)


       """
#Base cases
    if item not in empty:
        empty.append(item)  
                   
        if item not in data.keys():
            out_ls.append(item)
        elif item is data[item]:
            out_ls.append(item)
#Recursive case                
        elif item is not data[item]:
            item = data[item]
            recursion(data, item, out_ls, empty)
        
    else:
        out_ls.append(item)

   
 ############################################################################  
 

def bin(ls_int, lower_limits, out = None, cnt = None):

    """NOTE:I used RECURSION approach to solve both challenge

    Return the number of elements in each bin as a list.

    Args: 
        ls_int(list):a list of integers
        lower_limits(list):a list of the lower limit of bins
        
    Attributes:
        out(list): an instance of the output array

        cnt(int): A counter used to fill the output array

        
       """
    
    if out == None:
        out = []
        cnt = 1
      

    if type(ls_int[-1]) != int:
        raise AssertionError('Enter integers only')
        
      
      #Base case  
    if ls_int[-1] <= lower_limits[0]:
        out.append(cnt)
        return out[::-1]   
    #Recursive case
    elif ls_int[-1] > lower_limits[-1]:
        cnt+=1
        bin(ls_int[:-1], lower_limits, out, cnt)
    #Recursive case  
    elif ls_int[-1]<= lower_limits[-1]:
        out.append(cnt)
        cnt = 1
        bin(ls_int[:-1], lower_limits[:-1], out, cnt)
        
    return out[::-1]







"""
Double fold.
Part I:

Given a list of tokens (strings, integers or a combination) and a dictionary from token to token, write a function named  resolve to resolve each token and return a list of the resolved tokens in the same order. Resolving a token means repeatedly searching for it as a key in the dictionary and replacing it with the associated value until it cannot be found in the dictionary as a key. If there is an infinite loop of values or it is not in the dictionary, you should resolve a token to itself.

For example, if the dictionary is d = {'a': 'b', 'b': 'c', 'p': 'q', 'q': 'p'}, we resolve a to c, b to c, p to p, q to q, and z to z.

resolve(d, ['a','b','p','q','z']) returns ['c', 'c', 'p', 'q', 'z']

Explanation:

'a' maps to 'b' which maps to 'c' in the dictionary. c doesnt map to anything(i.e is not a key so it maps to itself)

'b' maps to 'c' which maps to itself

'p' maps to 'q' which maps to 'p' which maps to 'q' and it keeps going infinite;y. Hence we map 'p' to itself

'q' maps to 'q' just like p described above

'z' maps to itself as it isnt a key in the dictionary

Another example

d={'a':'b','b':'c','c':b}

resolve(d,['a','b']) returns ['b'.'b']

explantion is a maps to 'b' which maps to 'c' which maps to 'b' which maps to c(infinitely) so the answer is b

for the reason described above b maps to b also.

last example

d={'a':'b','b:'c','c':'a'}

resolve(d,['a']) will return ['a'] 

a maps to b which maps to c which maps back to a and the loop continues.

 

All keys should be alphabetic and integers positive.

 

Part II:

Bins are series of intervals that divide a range of integers into equal or unequal groups.

Given a list of integers and a list of the lower limit of bins, write a function named bin to return the number of elements in each bin as a list.

All integers are welcomed but the elements in the list of lower limit of bins should be in the range of the list of integers.

 

For example:

Given list(range(100)) and [0, 10, 25, 45, 70], you should return [10,15,20,25,30]

i.e bin(list(range(100)),[0,10,25,45,70]) will return [10,15,20,25,30]

bin([1,2,3,5,6,7,8,9,10,11,12],[2,5,10])  should return [2,5,3]  i.e 2 numbers between 2 and 5, 5 between 5 and 10 and 3 between 10 and infinity.

NOTE:

•No inbuilt module should be used.

•Raise AssertionErrors only
"""
print(bin([-2,1,2,3,5,6,7,8,9,10,11,12],[-2,5,10]))
