'''
滚动数组法
'''
#  递归方法
class solution1(object):
    def fibonacciNum(self):
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
    
#   动态数组
class solution2(object):
    def fibonacciNum(self):
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n):
            dp[i%3] = dp[(i-1)%3] + dp[(i-2)%3]      #因为连续变化的只有响铃三项，所以模3
        return dp[(n-1)%3]
'''
dp[0] = 1             i=0
dp[1] = 1             i=1
dp[2] = dp[0]+dp[1]   i=2
dp[0] = dp[1]+dp[2]   i=3
dp[1] = dp[0]+dp[2]   i=4
dp[2] = dp[1]+dp[0]   i=5
...
可以看到每一项都是前两项之和，且只用到了dp[0],dp[1],dp[2]三个存储空间
'''   

#二维数组情况---普通递归
class solution3(object):
    def sum(self):
        dp = [[0] * 10 for _ in range(10)]
        for i in range(10):
            dp[0][i] = 1
        for i in range(10):
            dp[i][0] = 1
        for i in range(1,100):
            for j in range(1,100):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
 '''
 dp[1][j] = dp[0][1] + dp[1][j-1]
 dp[2][j] = dp[0][j] + dp[2][j-1]
 dp[3][j] = dp[2][j] + dp[3][j-1]
 '''   


class solution4(object):
    def sum(self):
        dp = [[0] * 10 for _ in range(10)]
            for i in range(10):
                dp[0][i] = 1
            for i in range(10):
                dp[i][0] = 1
            for i in range(1,100):
                for j in range(1,100):
                    dp[i%2][j] = dp[(i-1)%2][j] + dp[i%2][j-1]   #发现只跟两行有关,dp[(i-1)%2][j]为dp[i%2][j]上边的数，dp[i%2][j-1]为dp[i][j]左边的数
            return dp[99%2][-1] 

 '''
 发现只跟两行有关,dp[(i-1)%2][j]为dp[i%2][j]上边的数，dp[i%2][j-1]为dp[i][j]左边的数
 i每次增加1，dp[i][j]都可以用dp[i%2][j]表
 '''           
        