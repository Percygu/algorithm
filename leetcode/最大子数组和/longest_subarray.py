class solution(object):
    def LongestSubArray(self,num):
        res = float("-inf")
        last=0
        for i in range(len(num)):
            now = max(last,0)+num[i]
            res = max(now,res)
            last = now
        return res

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    s = solution()
    print(s.LongestSubArray(arr))

            
