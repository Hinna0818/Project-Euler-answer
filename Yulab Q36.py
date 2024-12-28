def fun(n):
    num = str(n)
    if int(num[::-1]) == n:
        return True

def fun2(m):
    dp = []
    for i in range(m+1):
        bin_type = bin(i)[2:]
        if fun(i) and fun(int(bin_type)):
            dp.append(i)
    return sum(dp)

print(fun2(1000000))

