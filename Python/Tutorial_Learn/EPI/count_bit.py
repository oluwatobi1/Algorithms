def count_bits(x):
    '''
    Writing a program to count the number of bits that are set to 1 in a positive integer
    '''
    num_bit = 0
    while x:
        num_bit += x & 1
        x>>=1
    return num_bit

print(count_bits(21))