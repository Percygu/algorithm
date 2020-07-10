class solution(object):
    def RobSolution(self,nums):
        n = len(nums) 
        if n == 0:
            return 0
        dp = [0 for i in range(n+1)]    #初始化一个长度为n+1的数组,首元素初始化为0，让原数组从下标为1开始
        dp[0] = 0
        dp[1] = nums[0]             
        for i in range(2,n+1):          #从2到n
            print(i)
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])   
        return dp[n]                    #返回数组里的最后一个元素

if __name__ == "__main__":
    s = solution()
    nums = [0 for i in range(5)] 
    nums[0], nums[1],nums[2],nums[3],nums[4] = 2,7,9,3,1 
    print(s.RobSolution(nums))
