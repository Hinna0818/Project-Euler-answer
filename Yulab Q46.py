## 首先生成一个奇合数集合，然后遍历这个集合，对每一个奇合数n，遍历1到n
# 如果j是素数，那么n-j一定是合数，然后遍历1到n-j的平方根，如果n-j=2*x^2，那么n=j+2*x^2
# 找到这样的j和x，就说明n可以表示为一个素数加上两倍一个平方数，如果找不到这样的j和x，那么n就是我们要找的数。
def fun():
    from is_prime import is_prime
    odd_composite = {i for i in range(9,10000) if i%2!=0 and not is_prime(i)}
    for n in odd_composite:
        flag = False
        for j in range(1,n):
            if is_prime(j):
                for x in range(1, int((n-j)**0.5)+1):
                    if n == j + 2*x**2:
                        flag = True
                        break
            if flag:
                break
        if not flag:
            return n
print(fun())
    
