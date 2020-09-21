import random

def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(2, total, 2), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

print(constrained_sum_sample_pos(2, 717))
