def is_valid(arr):
    if arr.count(1)>9:
        return False
    current_index = len(arr)-1
    # print(current_index, arr, arr[current_index])
    if current_index == 0:
        return True
    elif 0 < current_index< 5:
        if (arr[current_index-1]==2) and (arr[current_index]==3):
            return False
        elif (arr[current_index-1]==3) and (arr[current_index]==2):
            return False
        else:
            return True

# for 5th/1st-(NB: zero indexing) cell in each row starting from the second row
    elif current_index%5==0:
        if  (arr[current_index-5]==3) and (arr[current_index]==2):
            return False
        elif  (arr[current_index-5]==2 or arr[current_index-4]==3) and (arr[current_index]==3):
            return False
        else:
            return True
# for fourth sell or last cell (NB:zero indexing) in each row starting from 2nd row 
    elif current_index+1%4==0:
        if  (arr[current_index-5]==3 or arr[current_index-6]==2) and (arr[current_index]==2):
            return False
        elif  (arr[current_index-5]==2) and (arr[current_index]==3):
            return False
        else:
            return True
# other cells in the middle
    elif (arr[current_index-1]==2 or arr[current_index-4]==3 or arr[current_index-5]==2) and (arr[current_index]==3):
        return False
    elif (arr[current_index-6]==2 or arr[current_index-5]==3 or arr[current_index-1]==3) and (arr[current_index]==2):
        return False
    else:
        return True

def solve(perm,n):
    # print(len(perm))
    if len(perm)==n:
        print(perm, " Answer")
        return

    for k in [3,2,1]:
        perm.append(k)
        if is_valid(perm):
            solve(perm, n)
        perm.pop()

arr1 =[]
print(arr1.count(1), " ones")
print(solve(arr1, n=25))