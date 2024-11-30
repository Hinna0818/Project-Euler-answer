def prime_sum(n):
    dp = []
    for i in range(2,n):
        if_prime = True
        for j in range(2,int(n**0.5)):
            if i % j == 0:
                if_prime = False
                break
        if if_prime:
            dp.append(i)
    return sum(dp)

prime_sum(2000000)