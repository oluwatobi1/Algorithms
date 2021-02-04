
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


phrase = 'hello world'

print(reverse(phrase))
print(reverse('123456789'))
print(reverse('hello'))
