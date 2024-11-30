def pythagorean():
    dp = []
    for a in range(1,1000):
        for b in range(1,1000-a):
            c = 1000-a-b
            if a**2 + b**2 == c**2 and a < b < c:
                dp.append((a,b,c))
    return dp

num = pythagorean()
print(num)
