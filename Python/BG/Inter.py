#take a list and find the number of occurence [0, 1, 2, 3, 3, 3] 
# the number of occurence
# 2=1

def number_of_occurence(array):
    if type(array)!=list:
        return "Not a list"

    if not len(array):
        return 'Empty list'    
    
    dct = {}
    for i in array:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
    return dct

array = [0, 1, 2, 3, 3, 3]

print(number_of_occurence([]))
print(number_of_occurence(0))
print(number_of_occurence(['random text']))
print(number_of_occurence('y'))