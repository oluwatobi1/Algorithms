s = 'banana'
def maxSubstring(s):
    maxchar = sorted(list(set(s)))[-1]
    index = [i for i in range(len(s)) if s[i]==maxchar]

    maxstring=''
    for i in range(len(index)):
        if (s[index[i]:len(s)]>maxstring):
            maxstring=s[index[i]:len(s)]

    return maxstring

print(maxSubstring(s))
