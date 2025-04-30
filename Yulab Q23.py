def find_abundant(n = 28123):
## 先找出所有abundant numbers
    dp = {}
    for i in range(1, n+1):
        flag = i
        dp[flag] = []
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                dp[flag].append(j)
                if j != i // j and i != i //j:  ## 去除自身为因数的情况
                    dp[flag].append(i//j) 
        dp[flag].sort()

    ## 求出所有abundant numbers
    dp_abundant = []
    for n in dp.keys():
        if sum(dp[n]) > n:
            dp_abundant.append(n)
    
    ## 对dp_abundant列表元素进行两两求和，使用集合去重
    dp_sum = set()
    for i in dp_abundant:
        for j in dp_abundant:
            if i+j <= n:
                dp_sum.add(i+j)
    
    all_num = set(range(1, n+1))
    non = all_num - dp_sum
    return sum(non)

find_abundant()

