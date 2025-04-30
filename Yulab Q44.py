def fun():
    pentagonal = {n*(3*n-1)//2 for n in range(1, 10000)}
    dp = []
    for i in pentagonal:
        for j in pentagonal:
            if i+j in pentagonal and abs(i-j) in pentagonal:
                dp.append(abs(i-j))
    return min(dp)

print(fun())

