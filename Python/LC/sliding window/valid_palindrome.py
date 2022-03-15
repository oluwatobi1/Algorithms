import string


def isPalindrome(self, s: str) -> bool:
    # using the walrus operator
    return (y := ''.join([i for i in s.lower() if i not in string.punctuation+" "])) == y[::-1]
