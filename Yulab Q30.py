def fun():
    dp = []
    for n in range(2, ((9**5)*6)+1):
        tmp = 0
        for j in str(n):
            tmp += int(j) ** 5
        if tmp == n:
            dp.append(n)
    return sum(dp)

a = fun()
print(a)
