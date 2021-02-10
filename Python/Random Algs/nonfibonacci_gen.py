# -Create a python generator to produce the 
# list of numbers not divisible by Fibonacci number
# 

def notfibgen2(no_of_iter):
    n, m = 0, 1 #initialize fibs
    count, num = 1, 1
    while count<=no_of_iter:
        n, m = m, n+m
        for i in range(n,m):
            #for each non-fib number 
            if i%2!=0 and i%3!=0 and i%5!=0 and i%13!=0:
                #if not divisible by the elementary fibs num excluding 1 (2,3,5,13)
                count+=1
                yield i
        
a = notfibgen2(1000)
for i in a:
    print(i)

#Note: since 0 & 1 are fibonnacci numbers
#  the output is supposed to be empty; 
# T'was delebrately ignored (maybe don't next time)
