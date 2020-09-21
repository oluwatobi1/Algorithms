def order(ls):
    """
    This takes an unsorted array of unique integers, and returns a tuple of 2 elements
    
    For example:
    Given [100, 4, 200, 1, 3, 2], 
    The function "order" returns (4,[100,200])
    where the longest consecutive elements sequence are [1,2,3,4] of len 4.
     
     
    Steps
    1. Manually sort the  input array
    2. Identify all the sequences in the sorted array
    3. Return the length of the longest sequence
    4. Remove the longest sequence and return the remaining item(int) sorted.
    5. Output in a tuple
    """
    
#######------Edge Cases checks
    if type(ls)!= list:
        return 'Error: Enter a List'
    else:
        for i in ls:
            if type(i)!=int:
                return 'Error: List must contain integers only'
    if len(ls)<2:
        return (0, ls)
    elif len(ls) == 2 & abs(ls[0]-ls[1])!=1:
        return "No sequence Found"

    
    
#######------Step 1
    my_sort = []
    
    while ls:
        minimum = ls[0]
        for i in ls:
            if i<minimum:
                minimum =i
        my_sort.append(minimum)
        ls.remove(minimum)
    
#######------Step 2
       
    my_seq=[[my_sort[0]]]   
    for i in range(1, len(my_sort)):
        if my_sort[i-1]+1 == my_sort[i]:
            my_seq[-1].append(my_sort[i])
            
        else:
            my_seq.append([my_sort[i]])
    
#######------Step 3
            
    seq = max(my_seq, key =len)
    len_of_seq = len(seq)
    
#######------Step 4 
   
    rem = []
    my_seq.remove(seq)
    for i in my_seq:
        rem.extend(i)
    
#######------Step 5 
       
    return (len_of_seq, rem)


print(order([100, 4, 200, 1, 3, 2]))