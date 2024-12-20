## 构建一个斐波那契数组，然后判断数字的位数
def fun(n):
    num = [1, 1]
    i = 1
    while len(str(num[i])) < n:
        num.append(num[i] + num[i - 1])
        i += 1
    return i + 1

result = fun(1000)
print(result)