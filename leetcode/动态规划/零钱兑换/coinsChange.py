# 完全背包：o(nm^2)  n为硬币数，m为金额数 
class solution1(object):
    def coinsChange(self,amount,coins):
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]   #初始化一个长度为n+1的数组,dp[i][j]表示在堆中加入了第i中硬币，凑出总价值为j的方案数
        dp[0][0] = 1                       #用面值为0的硬币凑出总价值为0的方案数有1种
        for i in range(1,amount+1):        #用面值为0的硬币凑出总价值为1到amount，每种的方案数都为0种。面值为0，不可能凑出价值大于0
            dp[0][i] = 0
        for i in range(1,n+1):
            dp[i][0] = 1                   #用面值为i的硬币凑出总价值为0的方案数为1种2，因为可以选前面已经加入到堆里的面值为0的硬币其凑
        for i in range(1,n+1):             #逐步将coins[0],coins[1]，...,coins[n-1]加入到堆中
            for j in range(1,amount+1):    #每加入一个，计算当前的总方案数
                k = 0
                while (j - k*coins[i-1])>=0:
                    dp[i][j] += dp[i-1][j - k*coins[i-1]]
                    k+=1
                    print("dp[%d][%d]=%d" % (i,j,dp[i][j]))
        return dp[n][amount]


# 优化状态转移方程   dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j],时间复杂度O(mn)
class solution2(object):
    def coinsChange(self,amount,coins):
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)] #初始化一个长度为n+1的数组
        dp[0][0] = 1                       #用面值为0的硬币凑出总价值为0的方案数有1种
        for i in range(1,amount+1):        #用面值为0的硬币凑出总价值为1到amount，每种的方案数都为0种。面值为0，不可能凑出价值大于0
            dp[0][i] = 0
        for i in range(1,n+1):
            dp[i][0] = 1                   #用面值为i的硬币凑出总价值为0的方案数为1种2，因为可以选前面已经加入到堆里的面值为0的硬币其凑
        for i in range(1,n+1):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j]      #初始化dp[i][j]为不加入第i中面值的硬币，前i-1中面值的硬币可以凑出j的方案数
                if j-coins[i-1]>=0:    #判断dp[i][j-coins[i-1]]是否存在
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
        return dp[n][amount]

# 优化存储空间  --滚动数组
class solution3(object):
    def coinsChange(self,amount,coins):
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)] #初始化一个长度为n+1的数组
        dp[0][0] = 1                              #用面值为0的硬币凑出总价值为0的方案数有1种
        for i in range(1,amount+1):               #用面值为0的硬币凑出总价值为1到amount，每种的方案数都为0种。面值为0，不可能凑出价值大于0
            dp[0][i] = 0
        for i in range(1,n+1):
            dp[i][0] = 1                          #用面值为i的硬币凑出总价值为0的方案数为1种2，因为可以选前面已经加入到堆里的面值为0的硬币其凑
        for i in range(1,n+1):
            for j in range(1,amount+1):
                dp[i%2][j] = dp[(i-1)%2][j]      #初始化dp[i][j]为不加入第i中面值的硬币，前i-1中面值的硬币可以凑出j的方案数
                if j-coins[i-1]>=0:              #判断dp[i][j-coins[i-1]]是否存在
                    dp[i%2][j] = dp[i%2][j-coins[i-1]] + dp[(i-1)%2][j]
        return dp[n%2][amount]
 

if __name__ == "__main__":
    s1 = solution1()
    s2 = solution2()
    s3 = solution3()
    coins = [1,2,5]
    amount = 5
    print(s1.coinsChange(amount,coins))
    print(s2.coinsChange(amount,coins))
    print(s3.coinsChange(amount,coins))





