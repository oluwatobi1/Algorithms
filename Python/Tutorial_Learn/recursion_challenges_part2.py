
def reverse(phrase):
    """
    This function takes in a string phrase and return the reverse
    using recursion..

    eg 
    reverse('the man ran') --> 'nar nam eth'
    print(reverse('123456789')) --> "987654321"
    reverse('hello') --> olleh
    """
    if len(phrase)==1:
        return phrase
    else:
        return reverse(phrase[1:])+phrase[0]

# phrase = 'hello world'

# print(reverse(phrase))
# print(reverse('123456789'))
# print(reverse('hello'))

def permute(s):

    out = []
    if len(s)==1:
        print([s])
        return s

    else:
        for i in range(len(s)):
            for perm in permute(s[:i]+s[i+1:]):
                out+=[s[i]+perm]
        return out
            





s = 'abc'

print(permute(s))
# print(permute('12389'))
# print(permute('hel'))

