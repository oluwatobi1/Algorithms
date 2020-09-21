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

    
print(bin([-2,1,2,3,5,6,7,8,9,10,11,12],[-2,5,10]))