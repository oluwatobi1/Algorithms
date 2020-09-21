def unique(ls):
    """
    This function takes a list(L) which contains numbers as a parameter and 
    returns a sorted new list with unique elements of the first list.
    
    steps
    1. Get the unique value into a list (un)
    2. Sort the unique value(sorting)
    3. Return the sorted list
    """
    # Edge case check
    if type(ls)!= list:
        return 'Error: Enter a List'
    else:
        for i in ls:
            if type(i)!=int:
                return 'Error: List must contain numbers only'
    
    
    un = []
    for i in ls:
        if i not in un:
            un.append(i)
            
            
    sorting = []
    while un:
        minimum = un[0]
        for num in un:
            if num<minimum:
                minimum = num
        sorting.append(minimum)
        un.remove(minimum)
     
    return sorting

print(unique(564))



#Question

'''Unique_Numbers

Create a function unique that takes a list(L) which contains numbers as a parameter and returns a sorted new list with unique elements of the first list.

Sample Inputs

1) unique([1,2,3,3,3,3,4,5])

2) unique([1,2,3,3,3,3,4,5,3,3,3,3,4,5,6,6,11,22,33,44])

3) unique([1,2,3,3,3,3,4,5,5,3,3,3,3,4,5,6,6,110,20,19,34])

Sample Output

1) Sample List: [1, 2, 3, 3, 3, 3, 4, 5]

    Unique List: [1, 2, 3, 4, 5]

2) Sample List: [1, 2, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 4, 5, 6, 6, 11, 22, 33, 44]

    Unique List: [1, 2, 3, 4, 5, 6, 11, 22, 33, 44]

3) Sample List: [1, 2, 3, 3, 3, 3, 4, 5, 5, 3, 3, 3, 3, 4, 5, 6, 6, 110, 20, 19, 34]

    Unique List: [1, 2, 3, 4, 5, 6, 19, 20, 34, 110]'''