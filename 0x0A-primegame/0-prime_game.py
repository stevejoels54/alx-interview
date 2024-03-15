#!/usr/bin/python3
""" Prime Game problem """


def isWinner(x, nums):
    """ Determine who wins the game """
    if x < 1 or nums is None:
        return None
    n = max(nums)
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    sieve = [i for i in range(n + 1) if sieve[i] == 1]
    if x > len(sieve):
        return None
    return "Maria" if len(nums) % 2 == 0 else "Ben"
