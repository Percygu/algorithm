'''
双指针法
'''

def get_shootings(nums,n,m):
    my_set = set()   # 用来保存已经击中了哪些气球
    i,j = 0,0
    res = -1         # 最终结果初始化为-1
    cnt = [ 0 for _ in range(m+1)]  # 用来记录每种颜色的气球集中的次数，比如cnt[2] = 0,表示颜色为2的气球没击中，因为气球编号从1开始，所以要m+1大小的数组
    while i <= j and j < n:
        cnt[nums[j]] += 1            # nums[j]表示射击的第j个气球的编号
        if nums[j] != 0:             # 表示击中了某种编号的气球
            my_set.add(nums[j])    
        if len(my_set) >= m:         # 击中的气球种类数已经达到了标准
            while i < j:
                if nums[i] != 0 and cnt[nums[i]] == 1:   # nums[i]这种颜色的气球有且只有一个
                    break
                cnt[nums[i]] -= 1
                i += 1
            if res == -1 or j - i + 1 < res:  # 更新res
                res = j - i + 1
        j += 1
    return res

if __name__ == "__main__":
    n = input()
    m = input()
    nums = []
    for i in range(int(n)):
        num = input()
        nums.append(int(num))
    print()     # 换行
    print(get_shootings(nums,int(n),int(m)))    
    
    