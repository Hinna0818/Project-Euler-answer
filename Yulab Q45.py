def fun():
    pentagonal_num = [i*(3*i-1)//2 for i in range(1, 100000)]
    hexagonal_num = [i*(2*i-1) for i in range(1, 100000)]

    for i in range(286, 100000):
        triangle_num = i*(i+1)//2
        if triangle_num in pentagonal_num and triangle_num in hexagonal_num:
            return triangle_num

#print(fun())
        
## 这里用集合查找更高效，集合使用哈希表实现，查找操作的平均时间复杂度为 O(1)
## 列表使用数组实现，查找操作的平均时间复杂度为 O(n)。
def fun2():
    pentagonal_num = {i*(3*i-1)//2 for i in range(1, 100000)}
    hexagonal_num = {i*(2*i-1) for i in range(1, 100000)}
    for n in range(286, 100000):
        triangle_num = n*(n+1)//2
        if triangle_num in pentagonal_num and triangle_num in hexagonal_num:
            return triangle_num

print(fun2())