def factorial(n):
    result = 1
    sum = 0
    for i in range(1,n+1):
        result = result * i
    result_str = str(result)

    for i in result_str:
        sum = int(i) + sum
    return sum

factorial(100)
