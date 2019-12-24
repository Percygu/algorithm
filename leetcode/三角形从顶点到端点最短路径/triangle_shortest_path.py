class solution1:
    def GetTrianglePath(self,nums):    #用nums这个二维数组来表示三角形
        f = [[ 0 for j in range(i+1)] for i in range(len(nums))]
        print(f)
        res = float('inf')
        for i in range(1,len(nums)):     #表示第i行
            for j in range(len(nums[i])):         #表示第i行的第j列
                f[i][j] = float('inf')    #每一步将f[i][j]初始化为负无穷
                if j > 0:                #f[i][j]表示从顶点到第i行，第j列的点的最短路径
                    f[i][j] = min(f[i][j],f[i-1][j-1] + nums[i][j])    #最短路径从左上方来
                if j < i:
                    f[i][j] = min(f[i][j],f[i-1][j] + nums[i][j])       #最短路径从右上方来
        #上面两侧for循环计算出了最后一排的所有最短路径，然后找出其中最短的即可
        for i in range(len(nums)):
            res = min(res,f[len(nums)-1][i])
        return res

if __name__ == "__main__":
    nums = [[ 0 for j in range(i+1)] for i in range(4)]    #初始化一个4行，每个元素都为0的三角形，总的来说也是一个二维数组
    nums[0][0],nums[1][0],nums[1][1],nums[2][0],nums[2][1],nums[2][2] = 2,3,4,6,5,7
    nums[3][0],nums[3][1],nums[3][2],nums[3][3] = 4,1,8,3
    
    #用了额外的空间
    s1 = solution1()
    print(s1.GetTrianglePath(nums))

    #滚动数组
    