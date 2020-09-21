def generateGrayarr(n): 
  
    # base case 
    if (n <= 0): 
        return
  
    # 'arr' will store all generated codes 
    arr = list() 
  
    # start with one-bit pattern 
    arr.append("0") 
    arr.append("1") 
  
    # Every iteration of this loop generates  
    # 2*i codes from previously generated i codes. 
    i = 2
    j = 0
    while(True): 
  
        if i >= 1 << n: 
            break
      
        # Enter the prviously generated codes  
        # again in arr[] in reverse order.  
        # Nor arr[] has double number of codes. 
        for j in range(i - 1, -1, -1): 
            arr.append(arr[j]) 
  
        # append 0 to the first half 
        for j in range(i): 
            arr[j] = "0" + arr[j] 
  
        # append 1 to the second half 
        for j in range(i, 2 * i): 
            arr[j] = "1" + arr[j] 
        i = i << 1
  
    # prcontents of arr[] 
    return arr

def bits_of_gray(n):
    """
    This function returns a list of the gray codes as described below.
    Example 
    When input is  2, the function  returns: ['00', '01', '11', '10']
    When input is 3 , the function  returns: [ '000', '001','011','010','110','111','101','100']
    
    Steps
    Note:An understanding of how binary works is needed.
    1. Get the range of digits in decimals and number of output using 2**n formula.
        ie 3 contains max of 8 possible outputs
        The range of output is easily represented by 0-8 in decimals
        
    2. Convert all digits within the range to decimal(manually)
    3. Append neccessary zeros
    4. Return answers
    """
    
    if type(n) != int:
        return "Input Error: function takes only integers!"
    
    ans = []
    
    for i in range(2**n):        
        binary = ''
        while i>0:
            reminder = i%2
            i=i//2
            binary=str(reminder)+binary
            
        out = '0'*(n-len(binary))+binary
        
        ans.append(out)

    return ans


def bits_of_gray2(n):
    if n <= 0:
        return []
    if n == 1:
        return ['0', '1']
    res = bits_of_gray2(n-1)
    return ['0'+s for s in res] + ['1'+s for s in res[::-1]]


def possible_bits(length):
    if length <=0:
        return []
    if length == 1:
        return ['0', '1']
    se = []
    res = possible_bits(length-1)
    ans = ['0'+ num for num in res]
    bas = ['1'+ num for num in res[::-1]]
    return ans + bas
print(possible_bits(3))
    
    


