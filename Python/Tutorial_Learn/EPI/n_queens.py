import itertools as it

def n_queens(perms):
    a = 0
    for (i1, i2) in it.combinations(range(len(perms)), 2):
        if abs(i1 -i2) == abs(perms[i1]-perms[i2]):
            return False
    return True


assert(n_queens([1,3,0,2])== True)
assert(n_queens([3,1,0,2])== False)
print(n_queens([3, 2,0, 1]))
print(n_queens([1, 3,0, 2]))

for perm in it.permutations(range(5)):
    if n_queens(perm):
        print(perm)
        exit()