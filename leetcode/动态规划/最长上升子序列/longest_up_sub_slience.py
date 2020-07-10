class solution(object):
    def LongestSubSlice(self,nums):
        n = len(nums) 
        dp = [0 for i in range(n+1)]         #初始化一个长度为n+1的数组
        dp[0] = 0                            #dp[i]表示nums中以第i个数字结尾的最长上升子序列的长度，对应于nums数组的下标为i-1
        dp[1] = 1                         
        for i in range(2,n+1):               #显然：以第i个数字结尾的最长上升子序列中最后一个数字是nums[i],倒数第二个数字可能是0到nums[i-1]中的任意一个数，从第2个数到第n个数
            dp[i] = 1                        #初始化以第一个数字结尾的最长上升子序列就是它本身，长度为1
            for j in range(1,i):             #子序列中倒数第以倒数二个数字结尾的最长上升子序列长度为dp[j],j=0,1,2,...i-1      
                if nums[j-1] < nums[i-1]:    #第i个数和第j个数作比较
                    dp[i] = max(dp[j]+1,dp[i])   #在上述这些以j结尾的子序列中，选择最长的
            print("i=%d,dp[%d]=%d" % (i,i,dp[i]))
        res = 0                             #用来记录最长的上升子序列，在所有的dp[i]中选择最大的
        for i in range(1,n+1):              #i对的下标从1到n
            res = max(res,dp[i])
        return res

if __name__ == "__main__":
    s = solution()
    nums = [0 for i in range(8)] 
    nums[0], nums[1],nums[2],nums[3],nums[4] = 10,9,2,5,3 
    nums[5], nums[6],nums[7] =  7,101,18 
    print(nums)
    print(s.LongestSubSlice(nums))
