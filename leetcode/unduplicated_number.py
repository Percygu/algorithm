'''
寻找数组里只出现一次的数字
'''
from typing import List

class Solution:
    def singleNUmber(self,nums: List[int])->int:
        no_duplicated_table = {}
        for i in nums:
            try:
                no_duplicated_table.pop(i)
            except:
                no_duplicated_table[i] = 1
                #no_duplicated_table.popitem()返回一个元祖
        return no_duplicated_table.popitem()[1]

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,4,2,4]
    d = {"a":1,"b":2}
    print(d)
    print(s.singleNUmber(nums))
