'''Generate an array of arrays of length X containing unique number that can sum up to Y. from array 1 to K.
if X=2, Y=10 and K=9.
Find generate all 2 unique numbers within 1 to 9 that will equal 10.
Answer:
[[1,9],[2,8],[3,7],[4,6]].
If X=3, Y=10, K=9.
Answer:[[1,2,7],[1,3,6],[1,4,5],[2,3,5]]

Note if you can't get any combination return an empty array

X, Y and K
X represents the length of the inner arrays, 
Y represents the number we are summing to.
K represents the maximum number each unique number can have'''

def summer(x, y, k):
    store = list(range(1,y))
    out = []
    uniques = set()
    for i in range(len(store)-x):
        slide = store[i:i+x-1]
        curr = y - sum(slide)
        if curr in store and curr not in slide and curr <k:
            mth = slide+[curr] 
            c = ''.join([str(i) for i in sorted(mth)])  
            if c not in uniques:
                out.append(mth)
                uniques.add(c)

    return out

x= 3
y=10
k=7
print(summer(x, y, k))





