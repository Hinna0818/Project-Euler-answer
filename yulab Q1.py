def add(N, x):
    n = (N-1) // x
    return sum([x * i for i in range(1, n+1)])

add(1000,3) + add(1000,5) - add(1000, 15)
