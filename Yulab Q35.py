def fun(n):
    from is_prime import is_prime
    dp = []
    
    for i in range(2, n+1):
        s = str(i)
        rotations = [int(s[i:] + s[:i]) for i in range(len(s))]  ## 循环移位计算循环数

        if all(is_prime(x) for x in rotations):
            dp.append(i)
        
    return len(dp)

a = fun(1000000)
print(a)