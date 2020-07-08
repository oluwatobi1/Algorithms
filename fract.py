def gcd(a, b): 
   
    # Everything divides 0  
    if (a == 0):  
        return b;  
    if (b == 0):  
        return a;  
      
    # base case  
    if (a == b):  
        return a;  
      
    # a is greater  
    if (a > b):  
        return gcd(a - b, b);  
    return gcd(a, b - a);  
      
# Function that will calculate 
# the Lcm of Numerator 
def LCM(num): 
    N  = len(num)
  
    ans = num[0]; 
    for i in range(1,N): 
        ans = (((num[i] * ans)) / (gcd(num[i], ans))); 
    return ans; 


print(LCM([4, 8]))