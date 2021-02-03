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


print(rec_sum(5))    