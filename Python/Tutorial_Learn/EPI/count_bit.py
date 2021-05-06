def count_bits(x):
    num_bit = 0
    while x:
        num_bit += x & 1
        x>>=1
    return num_bit

print(count_bits(21))