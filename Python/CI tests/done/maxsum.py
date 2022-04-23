def find_max(arr):
    incl = 0
    excl = 0
    
    for i in arr:
        #current max excluding i 
        new_excl = excl if excl>incl else incl
        
        #current max including i
        incl = excl + i
        excl = new_excl
    return (excl if excl>incl else incl)


print(find_max([30,15,60,75,45,15,15,45]))