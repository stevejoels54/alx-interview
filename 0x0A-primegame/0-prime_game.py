#!/usr/bin/python3
""" Prime Game problem """


# function to generate prime numbers using Sieve of Eratosthenes algorithm
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes


def isWinner(x, nums):
    """ Determine who wins the game """

    if not nums or x < 1:
        return None

    wins = {"Maria": 0, "Ben": 0}

    for i in range(x):
        num = nums[i]
        primes = generate_primes(num)
        if len(primes) % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    if wins["Maria"] < wins["Ben"]:
        return "Ben"
    return None
