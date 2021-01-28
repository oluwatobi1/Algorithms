

def solve(str_a, str_b):
    set_a = set(str_a)#A set has this property of Keeping unique item in it
    set_b = set(str_b)
    common_character = list(set_a & set_b)
    print( ''.join(common_character))

solve("adbc", "dfga")