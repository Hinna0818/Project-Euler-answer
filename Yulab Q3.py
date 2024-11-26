def max_prime(n):
    fs = []

    while n%2 == 0:
        fs.append(2)
        n //= 2
    
    f = 3
    while f*f <= n:
        while n%f == 0:
            fs.append(f)
            n //= f
        f += 2
    
    if n > 2:
        fs.append(n)

    return(max(fs))

result = max_prime(600851475143)
print(result)

    

        

