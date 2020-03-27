alp_dict = {'a':1,'b':3,'c':3,'d':2,'e':1
            ,'f':4,'g':2,'h':4,'i':1,'j':8
            ,'k':5,'l':1,'m':3,'n':1,'o':1
            ,'p':3,'q':10,'r':1,'s':1,'t':1
            ,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}

            

def word_score1(word):
    word = word.replace(' ', '').lower()
    score = 0    
    score = sum([score + alp_dict[word] for word in word])
    return score
        
print(word_score1(' ')) 

def score(word):
    return sum([alp_dict.get(letter, 0) for letter in word])
print(score('quizzify'))