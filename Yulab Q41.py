def fun():
    from is_prime import is_prime
    from itertools import permutations

    ## 从9位数开始，生成所有可能的组合数，然后判断是否为质数，最后把位数递减1
    digits = "123456789"
    max_prime = 0
    for n in range(9, 0, -1):
        pandigitals = permutations(digits[:n])
        for p in pandigitals:
            num = int(''.join(p))
            if is_prime(num) and num > max_prime:
                max_prime = num
    
    return max_prime

print(fun())
