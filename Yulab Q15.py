def calculation(n):
    tmp = 1
    for i in range(1, n+1):
        tmp = tmp * i
    return tmp

result = calculation(40) // calculation(20) **2
print(result)



## optimize for calculate factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)




