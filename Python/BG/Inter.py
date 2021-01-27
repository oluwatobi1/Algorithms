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
# second attempt
def number_of_occurence2(array):
    if type(array)!=list:
        return "Not a list"

    if not len(array):
        return 'Empty list'    
    uniques = set(array)    
    for i in uniques:
        print(f"{i} occurs in {array.count(i)} times")
        print(i, "occurs here ", array.count(i)," times")
 



array = [0, 1, 2, 3, 3, 3]

print(number_of_occurence2([]))
print(number_of_occurence2(0))
print(number_of_occurence2(['random text']))
print(number_of_occurence2('y'))
print(number_of_occurence2(array))