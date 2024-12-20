## a function using Sieve of Eratosthenes method to find primes under a expected input
def prime(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i]]

## test
prime(100)
