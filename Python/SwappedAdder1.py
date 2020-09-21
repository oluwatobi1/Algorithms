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
    
    ans = [numerator[i]/denominator[i] for i in range(len(numerator))]
    s = sum(ans)
    y = str(s).as_integer_ratio()
    print(numerator, denominator, ans, s, y)
    

    return y




def swap(a, b):
    a, b = b, a
    return a, b

print(adder(['1/2','1/3','1/6']))