## 用数学知识推导出两条对角线的元素的通项公式
## 易得：一个k阶矩阵一共有（k+1）/2层，通项公式见result部分，两条对角线分别求然后相加
def fun(k):
    n = (k+1)//2
    result = 0
    for i in range(1, n+1):
        if i == 1:
            result = 1
        else:
            result += 4*(2*i-1)**2 - 12*(i-1)
    return result

a = fun(1001)
print(a)
            
