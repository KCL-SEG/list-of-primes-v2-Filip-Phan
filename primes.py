"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    for i in range(2, int(number/2) + 1):
        if (number % i) == 0:
            return False

    return True

def primes(number_of_primes):

    if number_of_primes <=0:
        raise ValueError("Please enter a number that is larger than 0")

    list = []
    current = 2

    while len(list) < number_of_primes:
        if isPrime(current):
            list.append(current)
        current = current + 1


    return list
