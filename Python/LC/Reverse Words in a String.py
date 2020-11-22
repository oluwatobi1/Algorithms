def reverseWords(s: str):
    return ' '.join(s.split()[::-1])

def reverseWords2(s: str)->str:
    i=0
    start = False
    counter = 0
    words =[]
    while i<len(s):
        if s[i] !=" " and not start:
            start=True
            counter=i            
        elif s[i]==' ' and start:
            start = False
            words.append(s[counter:i])            
            counter=0
        i+=1
    if start:
        words.append(s[counter:len(s)])
    return ' '.join(words[::-1])       

s = "the sky is blue"
print(reverseWords2(s))