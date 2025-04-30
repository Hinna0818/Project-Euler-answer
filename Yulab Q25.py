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

## 当然不用列表存也可以，这样减少了空间的占用
def fun_update(n):
    a, b = 1, 1
    i = 2
    while len(str(b)) < n:
        a, b = b, a+b
        i += 1
    return i

result2 = fun_update(1000)
print(result2)