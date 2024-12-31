def fun(n):
    max_len = 0
    for i in range(1, n+1):
        dp = []
        for a in range(1, i//2):
            for b in range(a, (i-a)//2+1):
                c = i-a-b
                if a*a + b*b == c*c:
                    dp.append((a,b,c))
                if len(dp) > max_len:
                    max_len = len(dp)
                    result = i
    return result

print(fun(1000))