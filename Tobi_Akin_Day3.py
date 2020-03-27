def bin_search(sorted_list, item):
    '''Returns a boolean indicating whether the value(number) is in the list or not'''
    f, nf= 'Found', 'Not found'
    if item > sorted_list[-1]:
        return print(nf)
    elif item < sorted_list[len(sorted_list)//2]:
        sorted_list = sorted_list[:len(sorted_list)//2]
        bin_search(sorted_list, item)
    elif item > sorted_list[len(sorted_list)//2]:
        sorted_list = sorted_list[len(sorted_list)//2+1:]
        bin_search(sorted_list, item)
    elif sorted_list[len(sorted_list)//2] == item:
        return print(f)
    else:
        return print(nf)
    
    
bin_search([1,2,3,5,8], 10)


def bin_search2(lst, num):
    first = 0
    last = len(lst)-1
    found = False
    while (first<=last and not found):
        mid = (first - last)//2
        if lst[mid] == num:
            found = True
        elif lst[mid]<num:
            last = mid-1
        else:
            first = mid-1
            
    return found
          
          
            
bin_search2([1,2,3,5,8], 20)