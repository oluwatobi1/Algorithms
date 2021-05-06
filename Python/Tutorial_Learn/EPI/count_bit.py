def count_bits(x):
    '''
    Writing a program to count the number of bits that are set to 1 in a positive integer
    '''
    num_bit = 0
    while x:
        num_bit += x & 1
        x>>=1
    return num_bit

def parity(d):
    """
    The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. For
    example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
    single bit errors in data storage and communication.
    """

    result = 0
    while d:
        result ^= d & 1
        d>>=1
    return result

print(parity(8392))