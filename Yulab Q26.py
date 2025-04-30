def fun(d):
    max_len = 0
    max_i = 0
    
    for i in range(1, d):
        remainders = {}
        value = 1
        position = 0
        
        while value != 0 and value not in remainders:
            remainders[value] = position
            value *= 10
            value %= i
            position += 1
        
        if value != 0:  # 找到循环节
            cycle_length = position - remainders[value]
            if cycle_length > max_len:
                max_len = cycle_length
                max_i = i
    
    return {max_len: max_i}

a = fun(1000)
print(a)