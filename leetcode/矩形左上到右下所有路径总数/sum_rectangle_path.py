class solution(object):
    def GetSumOfPath(self,obstacleGrid):
        m = len(obstacleGrid)             #m行
        n = len(obstacleGrid[0])         #n列
        dp = [[0]*n for _ in range(m)]  #初始化一个m行n列，元素全为0的矩阵dp，用来记录到达每一个矩阵中每一个元素的路径和
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0  #若果第一个元素，即左上角元素为nums[1][1]==1,为障碍物
        if dp[0][0] == 0:
            return 0    #起点为障碍物，无法走到右下角
        for i in range(0,n):       #计算第一行
            if obstacleGrid[0][i] == 1:   #nums[0][i]这个点为障碍物，走不到这个点
                dp[0][i]=0       
                break
            else: 
                dp[0][i]=1      #能走到nums[0][i]这个点，总共只有一种走法，因为只能从起点往右走
        for i in range(0,m):      #计算第一列
            if obstacleGrid[i][0] == 1:  #nums[i][0]这个点为障碍物，走不到这个点
                dp[i][0] = 0
                break
            else: 
                dp[i][0] = 1     #能走到nums[i][0]这个点，总共只有一种走法，因为只能从起点往下走
        for i in range(1,m):    #去除第一行
            for j in range(1,n):   #去除第一列
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == "__main__":
    #构造一个0-1矩阵
    nums = [[0]*3 for _ in range(3)]
    nums [1][1] = 1

    print(nums)
    s = solution()
    print(s.GetSumOfPath(nums))
