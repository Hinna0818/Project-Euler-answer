## 这题本质是求1-20的最小公倍数，寻找最小公倍数的算法
from math import gcd

# 计算 1 到 n 的最小公倍数
def find_lcm(n):
    lcm = 1
    for i in range(1, n + 1):
        lcm = lcm * i // gcd(lcm, i)  
    return lcm

result = find_lcm(20)
print(result)  # 输出最小公倍数
