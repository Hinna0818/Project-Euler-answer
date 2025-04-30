## 写一个函数从左到右和从右到左判断质数
def is_truncatable_prime(num):
    from is_prime import is_prime
    a = str(num)
    for i in range(len(a)):
        if not is_prime(int(a[i:])):
            return False
    for i in range(len(a)):
        if not is_prime(int(a[:len(a)-i])):
            return False
    return True

def fun():
    from is_prime import is_prime
    i = 11  ## 从两位数的质数开始
    dp = []
    while len(dp) < 11:
        if is_prime(i) and is_truncatable_prime(i):
            dp.append(i)
        i += 2
    return sum(dp)

print(fun())
