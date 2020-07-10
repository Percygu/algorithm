class solution(object):
    def strangePrinter(self,s):
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)] #初始化一个n+1 * n+1的二维数组，下标从1开始 dp[i][j]表示打印第i个字母到第j个字母所需要的最少次数
        for i in range(n+1):
            dp[0][i] = 0
            dp[i][0] = 0
        if n == 1:
            return 1                           #只有一个字符
        for j in range(2,n+1):                 #分两步思考。第一步尽可能多的从左往右打印，打印成最终左边的都一样的字符串
            for i in range(1,j):               #两层循环穷举出所有的区间
                dp[i][j] = dp[i+1][j] + 1      #初始化dp[i][j],最终字符串左边只有一个字母相同，还需要打印右边的第i+1到第j个字母
                while k<                       




