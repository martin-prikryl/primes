'''
Infinite primes iterator using Sieve of Eratosthenes
'''

import itertools

class Primes:
    '''
    Primes iterator
    '''
    def __init__(self):
        self.sieve = itertools.count(2)

    def __iter__(self):
        return self

    def __next__(self):
        next_prime = next(self.sieve)
        self.sieve = itertools.filterfalse(lambda number: number % next_prime == 0, self.sieve)
        return next_prime
