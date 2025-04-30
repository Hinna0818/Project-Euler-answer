def fun():
    dp = []
    for a in range(2, 101):
        for b in range(2, 101):
            dp.append(a**b)
    return len(set(dp))

a = fun()
print(a)