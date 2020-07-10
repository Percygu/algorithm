class solution:
    def GetSumOfDecodings(self,str):
        n = len(str)
        dp = [0 for i in range(n)]    #初始化一个长度为n，每个元素都为0的数组dp
        if n == 1:
            return 1
        dp[0] = 1
        for i in range(1,n):          #dp[i]表示以下标为i的字母结尾对的解码数
            if i == 1:
                t = (ord(str[0])-ord('0')) * 10 + (ord(str[i])-ord('0'))    #首先判断最后两个字母能不能联合到一起解码
                if t >= 10 and t <= 26:       #最后两个字符可以联合解码
                    dp[i] = 1
            if str[i] != '0':                 #str[i]可以单独解码
                dp[i] += dp[i-1]
            if i>= 2:
                t = (ord(str[i-2])-ord('0')) * 10 + (ord(str[i-1])-ord('0'))
                if t >= 10 and t <= 26:
                    dp[i] += dp[i-2]
        return dp[n-1]

if __name__ == "__main__":
    s = solution()
    print(s.GetSumOfDecodings('21216'))    
    
