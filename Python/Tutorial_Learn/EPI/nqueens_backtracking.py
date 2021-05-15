def can_extend_to_solution(perm):
    j = len(perm)-1
    for k in range(j):
        if j-k == abs(perm[k]-perm[j]):
            return False
    return True


def extend(perm, n):
    if len(perm) == n:
        print(perm)
        return

    for k in range(n):
        if k not in perm:
            perm.append(k)
            if can_extend_to_solution(perm):
                extend(perm, n)
            perm.pop()


print(extend(perm=[], n=5))