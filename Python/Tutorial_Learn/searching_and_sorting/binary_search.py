def binary_search(arr, ele):

    start = 0
    end = len(arr)
    middle = (end-start)//2
    found = False

    while len(arr) != 0 and not found:
        if ele == arr[middle]:
            found = True

        elif arr[middle] < ele:
            start = middle
            arr = arr[start:]
            middle = len(arr) // 2
        else:
            end = middle
            arr = arr[:end]
            middle = len(arr) // 2

    return  found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binary_search(arr, 1))
