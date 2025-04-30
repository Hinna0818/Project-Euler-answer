from is_prime import is_prime

def prime_factors_count(n, primes):
    count = 0
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            count += 1
            while n % prime == 0:
                n //= prime
    if n > 1:
        count += 1
    return count

def fun():
    limit = 1000000
    primes = [i for i in range(2, int(limit ** 0.5) + 1) if is_prime(i)]
    consecutive_count = 0

    for num in range(2, limit):
        if prime_factors_count(num, primes) == 4:
            consecutive_count += 1
            if consecutive_count == 4:
                return [num - 3, num - 2, num - 1, num][0]
        else:
            consecutive_count = 0

print(fun())