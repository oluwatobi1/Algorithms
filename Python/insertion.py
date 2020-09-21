def insertion(nlist):
    if type(nlist) != list:
        return AssertionError('Enter a list type')
    elif len(set(type(i) for i in nlist))>1:
        return AssertionError("List must contain single 'data type' only")
 
    for index in range(1,len(nlist)):
        currentvalue = nlist[index]
        position = index

        while position>0 and nlist[position-1]>currentvalue:
            nlist[position]=nlist[position-1]
            position = position-1

        nlist[position]=currentvalue
    return nlist


#print(insertion(['c','y','s']))

    
def biggie(arr, idx):

    if type(arr) != list or type(idx) != int:
        return AssertionError("Enter a 'list' type for Array; And 'integer' for index")
    elif len(set(type(i) for i in arr))>1:
        return AssertionError("List must contain single 'data type' only")

    return min((val<=arr[idx],abs(i-idx),val)for i,val in enumerate(arr))[2]


#print(biggie( [4, 1, 3, 5, 6], 0))