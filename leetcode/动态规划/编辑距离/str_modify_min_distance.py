class solution(object):
    def minDistance(self,word1,word2):
        n,m= len(word1),len(word2)                   #dp[i][j]将第一个字符串的前i个字母转换成第2个字符串的前j个字母的方案数,所以i有n个，j有m个
        dp = [[0] * (m+1) for _ in range(n+1)]       #初始化一个n+1行m+1列的二维数组
        for i in range(n+1):                           #初始化边界情况
            dp[i][0] = i                             #将第一个字符串的前i个字母转换成第个字符串的前0个字母需要i步，即一次一个字母删除i次即可
        for i in range(m+1):                           #将第一个字符串的前0个字母转换成第个字符串的前i个字母需要i步，即一次一个字母添加i次即可
            dp[0][i] = i 
        for i in range(1,n+1):                       # i 从1 到 n
            for j in range(1，m+1):                     # j 从1 到 m
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1    #添加和删除的情况
                exchangeNum = 0
                if word1[i-1] == word2[j-1]:
                    exchangeNum = dp[i-1][j-1]
                else:
                    exchangeNum = dp[i-1][j-1]+1
                dp[i][j] = min(dp[i][j],exchangeNum)
        return dp[n][m]

'''
word1: - - - - - - -
word2: - - - - - -
第一个字符串的前i个字母转换成第2个字符串的前j个字母的方案数
考虑最后一步：即在第一个字符串的基础上添加，删除或者修改一个字符就完成了将第一个字符串的前i个字母转换成第2个字符串的前j个字母
1.添加。 添加完成则说明word1的前i个字母已经和word2的前j-1个字母匹配上了，再加最后一个字母即word2[j]就可以和word2的前j个字母匹配上dp[i][j] = dp[i][j-1]+1
2.删除。 删除则说明word1的前i-1个字母已经和word2的前j个字母匹配上了，把多余的最后一个即第i个字母删除就刚好匹配。则dp[i][j] = dp[i-1][j] + 1 
3.修改。1.word1[i]==word2[j],则只需要前面的i-1个和j-1个匹配上了就行
3.修改。2.word1[i]!=word2[j],在前面的i-1个和j-1个匹配上了的基础上还要多加一步，把word1的第i个字母修改为word2的第j个字母
'''




