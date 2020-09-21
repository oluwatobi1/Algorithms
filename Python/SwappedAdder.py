def factors(a, b):
    '''
    Euclidean algorithm of two numbers is the largest number that divides both of them. 
    A simple way to find GCD is to factorize both numbers and multiply common factors.
    '''
    if a == 0: 
        return b 
    return factors(b%a, a)
      

def adder(ls):
    numerator = [None]*len(ls)
    denominator = [None]*len(ls)

    #to split the string for the numerator and denominator
    for i, frac in enumerate(ls):
        if '/' in frac and len(frac)>2:
            fraction = frac.split('/')
            numerator[i] = int(fraction[0])
            denominator[i] = int(fraction[1])
        else:
            raise AssertionError('Invalid Fraction found')

    # to get the lcm in the denominator
    ans = denominator[0]; 
    for i in range(1,len(numerator)): 
        ans = ((denominator[i] * ans) / (factors(denominator[i], ans)))

    #compute the fraction addition for the numerator (elementary maths)
    add = sum([ans/denominator[i]*numerator[i] for i in range(len(ls))])
    #gets a common factor for both num and denom and divides them to get the lowest form   
    reeduce = factors(add, ans)
    add = int(add/reeduce)
    ans = int(ans/reeduce) 
    #Returns in string format
    return str(add)+'/'+ str(ans)




def swap(a, b):
    a, b = b, a
    return a, b
