def fun(n):
    dp = []
    for i in range(1, n+1):
        dp.append(i**i)
    x = str(sum(dp))
    return x[-10:]

print(fun(1000))
