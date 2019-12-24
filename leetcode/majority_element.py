#求众数
from typing import List
from math import sqrt
import collections

#O(n复杂度)
class Solution1:
    def FindMajorityEle(self,nums: List[int]) -> int:
        numMap = collections.Counter(nums)  #将列表nums转化为一个字典,key为列表元素，value为列表元素出现的次数 
        #print(numMap.get(1))
        '''
        numMap.keys()为待排序迭代器，key=numMap.get为排序规则，即按照什么方式排序取最大值
        这里相当于迭代器里的每个元素都可以用作可以key指定的函数的参数/其key函数求得的值做排序
        但返回值返回的的key函数求得的值所对应的迭代器里的参数
        '''
        return max(numMap.keys(), key=numMap.get) 

#O(n^2复杂度)
class Solution2:
    def FindMajorityEle(self,nums: List[int]) -> int:
        for elem in nums:
            '''
            1 for item in nums if item == elem 返回一个列表，列表元素全为1，列表元素个数为满足条件if条件的个数
            在对1 for item in nums if item == elem 推导式生成的列表所有元素求和
            '''
            count = sum(1 for item in nums if item == elem)
            if count >= len(nums)//2:
                return elem


#时间复杂度O(nlgn)-----对列表排序，因为众数个数大于n/2，所以排完序后的列表下标为n/2的元素必为众数
class Solution3:
    def FindMajorityEle(self,nums:List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

#时间复杂度O(n)-----投票法https://leetcode-cn.com/problems/majority-element/solution/qiu-zhong-shu-by-leetcode-2/
class Solution4:
    def FindMajorityEle(self,nums:List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
  

if __name__ == "__main__":
    s1 = Solution1()
    s2 = Solution2()
    list = [1,2,3,4,2,1,3,1,1,1]
    print(s1.FindMajorityEle(list))
    print(s2.FindMajorityEle(list))

    a = range(1, 11)
    b = range(1, 10)
    print(a)
    print(b)
    c = sum([item for item in a if item in b])
    print(c)