## 要求两个三位数乘起来是一个最大的回文数，不妨直接假设这个最大的回文数是六位数
## 从最小的六位数100000开始，先求出最小的三位数，在这基础上继续循环
def palindrome():
    a = int(100000 ** 0.5) + 1
    b = a
    palindrome = {}

    while a <= 999:
        b = a
        while b <= 999:
            num = str(a*b)
            if num == num[::-1]:
                palindrome[(a,b)] = a*b
            b = b+1
        a = a+1

    max_ab = max(palindrome, key = palindrome.get)
    max_value = max(palindrome.values())

    print(max_ab)
    print(max_value)

palindrome()
        


