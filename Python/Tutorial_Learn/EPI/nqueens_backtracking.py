def generate_permutations(perm, n):
    if len(perm) == n:
        print(perm)
        return

    for k in range(n):
        if k not in perm:
            perm.append(k)
            generate_permutations(perm, n)
            perm.pop()

print(generate_permutations(perm=[], n=5))