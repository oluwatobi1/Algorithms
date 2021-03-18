

def seq_search(arr, ele):
    position = 0
    found = False

    while position < len(arr) and not found:
        if arr[position] == ele:
            found = True
        else:
            position += 1
    return found


def ordered_seq_search(arr, ele):
    position = 0
    found = False
    stop = False

    while position < len(arr) and not found and not stop:
        if arr[position] == ele:
            found = True
        else:
            if arr[position] > ele:
                stop = True
            position += 1
    return found


arr1 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
print(ordered_seq_search(arr1, 4))


