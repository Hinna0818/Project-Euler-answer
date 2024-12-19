## 使用递归求解0-9数字的全排列组合，然后取第1000000位置的元素即可
def fun(num):
    result = []
    n = len(num)

    if n == 0: ## 递归终止
        return [[]]

    for i in range(n):
        current = num[i]
        remaining = num[:i] + num[i+1:]

        for p in fun(remaining):  
            result.append([current]+p)
    return result

number = list(range(10))
a = fun(number)
print(a[1000000-1])
