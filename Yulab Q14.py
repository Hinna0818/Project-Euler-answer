def chain(n):
    max_len = 1  ## 初始化链条最大长度
    num = 1 ## 初始化链条的第一个元素
    max_dp = [] ## 初始化最大链条

    for i in range(2, n+1):
        dp = [i]
        a = i
        
        while a != 1:
            if a%2 == 0:
                a = a//2
            else:
                a = 3*a+1
            dp.append(a)
        
        if max_len < len(dp):
            max_len = len(dp)
            num = i
            max_dp = dp
    
    return num, max_len, max_dp

chain(1000000)

        

        
        