import re, string
def is_Nigerian(strng): 
    '''Returns a boolean value to validating Nigerian Phone numbers'''    
    strng = re.sub('[ +-]', '', strng)
    if len(strng)< 11:
        print('no')
        return False
    elif strng.startswith(('080','081','090','070')) and len(strng) == 11:
        print('yes')
        return True
    elif strng.startswith('234') and len(strng)== 13:
        print('yes')
        return True 
    else:
        print('NO')
        return False   


    
def is_Nigerian2(s):
    s= s.translate(str.maketrans({'+': '', ' ': '', '-': ''}))
    pattern = re.compile(r'^(0)(7|8|9)(0)|^081')
    ptn = re.compile(r'^234')
    return True if (re.search(pattern, s) and len(s) == 11) or (re.search(ptn, s) and len(s)== 13) else False

print(is_Nigerian2('08140309'))

    
    
