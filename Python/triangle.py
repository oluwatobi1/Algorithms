def Triangle_no(n):
    if n<0:
        raise AssertionError('Number can\'t be negative.')
    
    return ((8*n+1)**0.5 - 1)/2 == int(((8*n+1)**0.5 - 1) / 2)

