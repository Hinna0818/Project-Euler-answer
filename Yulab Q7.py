def prime(n):
    dp = []
    num=2
    while len(dp) <= n:
        is_prime = True
        for i in range(2,int(num*0.5)+1):
            if num % i == 0:
                is_prime = False
                break  ## break就说明num不是质数，直接让num+1
        if is_prime:
            dp.append(num)
        num+=1
    return dp

a = prime(10001)
print(a[10000])