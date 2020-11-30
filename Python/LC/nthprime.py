def nth(n):
    store={}
    for i in range(n):
        store[i]=1
    store[0]=0
    store[1]=0
    for i in range(2, n):
        if store[i]==1:
            j=2
            while i*j<n:
                store[i*j]=0
                j+=1
    return store

print(nth(20))
