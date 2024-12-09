def amicable_num(n):
    dp = {}
    b = []
    for i in range(1, n+1):
        a = []
        for j in range(1, i):
            if i % j == 0:
                a.append(j)
        dp[i] = sum(a)
    
    for i in dp:
        j = dp[i]
        if j != i and j <= n and dp.get(j) == i:
            b.append(i)
    
    return sum(b)

amicable_num(10000)

        


