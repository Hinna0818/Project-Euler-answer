## 首先写一个判断pandigital的函数，然后循环1到n，分别与某个数相乘
# 看看是否等于一个pandigital数，如果是，就加入到一个集合中。最后返回最大的pandigital数

## 判断pandigital数
def is_pandigital(n):
    n = str(n)
    if len(n) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in n:
            return False
    return True

## 主函数
def fun():
    pandigitals = set()
    for n in range(1, 10000):
        product = ''
        i = 1
        while len(product) < 9:
            product += str(n * i)
            i += 1
        if is_pandigital(int(product)) and len(product) == 9:
            pandigitals.add(int(product))
    return max(pandigitals)

print(fun())

   



            

