def change(num):
    assert(num >=8)

    if num == 8:
        return [3,5]
    if num == 9:
        return [3 ,3 ,3]
    if num == 10:
        return [5, 5]

    coins = change(num-3)
    coins.append(3)
    return coins

print(change(45))