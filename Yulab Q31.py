## 使用动态规划算法，dp为一个列表，dp[i]表示凑成i的方法数
## 先初始化dp都为0，然后依次对每个硬币值进行遍历，更新dp[i]的方法数
def fun(target):
    a = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [0] * (target + 1)
    dp[0] = 1  # 只有一种方法可以凑成0，就是不使用任何硬币

    for coin in a:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

a = fun(200)
print(a)