def fun(limit):
    from is_prime import is_prime
    primes = [i for i in range(2, limit+1) if is_prime(i)]
    primes_set = set(primes)
    max_length = 0
    max_prime = 0

    for i in range(len(primes)):
        prime_sum = 0
        for j in range(i, len(primes)):
            prime_sum += primes[j]
            if prime_sum >= limit:
                break
            if prime_sum in primes_set:
                current_length = j - i + 1
                if current_length > max_length:
                    max_length = current_length
                    max_prime = prime_sum

    return max_prime, max_length

print(fun(10000000))
