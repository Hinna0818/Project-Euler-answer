from is_prime import is_prime ## 导入提前写好的判断素数的函数

def fun():
    dp = {}  ## 用字典存储每个i,j对应的素数个数，最后可以返回系数的乘积
    max_value = 0
    max_i = 0
    max_j = 0
    for i in range(-999, 1000):
        for j in range(-1000, 1001):
            dp[(i, j)] = 0
            n = 0
            while True:
                value = n**2+i*n+j
                if value < 0:
                    break
                if is_prime(value):
                    dp[(i, j)] += 1
                    n += 1
                else:
                    break
        
            if dp[(i, j)] > max_value:
                max_value = dp[(i, j)]
                max_i = i
                max_j = j
    return max_i*max_j

a = fun()
print(a)




