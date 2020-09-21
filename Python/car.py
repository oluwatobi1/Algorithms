def my_cars(arr):
    '''
    This takes in the array and RETURNS the maximum sum 
    with the condition that you can't select  2 numbers that are beside each other.
    i.e There must be at least one number or more between any 2 numbers chosen.
    Example 
    
    my_cars([30,15,60,75,45,15,15,45])
    will return 180
    
    
    '''
    
    
     # Edge case check
    if type(arr)!= list:
        return 'Error: Enter a List'
    else:
        for i in arr:
            if type(i)!=int:
                return 'Error: List must contain numbers only'
    
    
    staff = 0
    rod = 0
    
    for i in arr:
        new_rod = rod if rod > staff else staff
        staff = rod + i
        rod = new_rod
        
    return (rod if rod>staff else staff)

print(my_cars([60,75,45,15,15,45]))
