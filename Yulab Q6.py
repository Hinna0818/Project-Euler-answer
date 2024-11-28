def sum1(n):
    ans = 0
    for i in range(1,n+1):
        ans = ans + i*i
    return ans

def sum2(m):
    ans = 0
    for i in range(1,m+1):
        ans += i
    return ans*ans
sum2(100)-sum1(100)