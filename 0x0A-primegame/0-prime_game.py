#!/usr/bin/python3
""" Prime Game problem """


def is_prime(n):
    """ Determine if a number is prime """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    """ Generate a list of prime numbers """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
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
