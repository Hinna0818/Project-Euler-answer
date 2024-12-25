from math import factorial

def fun():
    factorials = [factorial(i) for i in range(10)]  # 预先计算 0 到 9 的阶乘
    dp = []
    for i in range(10, 1000000):  # 从 10 开始，因为 1 和 2 不算在内
        if sum(factorials[int(x)] for x in str(i)) == i:
            dp.append(i)
    
    return sum(dp)  # 返回符合条件的数字之和

a = fun()
print(a)