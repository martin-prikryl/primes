#!/usr/bin/python3
'''
Primes generator using Sieve of Eratosthenes
Use -l to limit output or use Ctrl+C to interrupt.
'''

import argparse
import sys
from primes import Primes

argument_parser = argparse.ArgumentParser('Primes generator')
argument_parser.add_argument('-l', dest='limit', type=int, default=None)
limit = argument_parser.parse_args().limit

prime_numbers = Primes()
for prime in prime_numbers:
    if limit and prime > limit:
        sys.exit()
    print(prime)
