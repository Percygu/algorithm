'''
求字符串中的最长回文子串
'''

#中心扩散法
class Solution1:

    #中心扩散
    def CenterPread(self,s,size,left,right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数,从一个相同的字符开始往两边扩散
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数，从两个不同的字符开始往两边扩散
        """
        l = left
        r = right
        while l>=0 and r < size and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r],r-l-1   #返回子串和子串长度
       
    def LongestPalinDrome(self,s):
        size = len(s)
        if size == 0:
            return ''
        dp = [[False for _ in range(size)] for _ in range(size)]  #用False初始化一个size * size的二维数组
        print(dp)

        # 字符串不为空，回文长度至少是1
        longest_palindrome = 1
        longest_palindrome_str = s[0]

        # i从下标0开始变化
        for i in range(size):
            palindrome_odd, odd_len = self.CenterPread(s, size, i, i)   #回文长度为基数情况
            palindrome_even, even_len = self.CenterPread(s, size, i, i + 1) #回文长度为偶数情况       
            #当前找到的最长回文子串,取基数和偶数中较长的
            current_max_sb = palindrome_odd if odd_len > even_len else palindrome_even
            #替换当下最长子串和子串长度
            if len(current_max_sb) > longest_palindrome:
                longest_palindrome = len(current_max_sb)
                longest_palindrome_str = current_max_sb
        
        return longest_palindrome_str


#动态规划方法
class Solution2:
    def LongestPalinDrome(self,s):
        size = len(s)
        if size == 0:
            return ''
        if size == 1:
            return s
       
        #采用dp[l][r]来表示字符串s是不是回文串，l为s的做下标，r为s的由下标
        
        longest_palindrome = 1           #初始化最长回文子串长度为1
        longest_palindrome_str = s[0]    #初始化最长回文子串长度为第一个字符




if __name__ == "__main__":
    s1 = Solution1()
    print(s1.LongestPalinDrome("babad"))




'''
推荐理由：暴力解法太 naive，中心扩散不普适，Manacher 就更不普适了，是专门解这个问题的方法。而用动态规划我认为是最有用的，可以帮助你举一反三的方法。

补充说明：Manacher 算法有兴趣的朋友们可以了解一下，有人就借助它的第一步字符串预处理思想，解决了 LeetCode 第 4 题。因此以上推荐仅代表个人观点。

解决这类 “最优子结构” 问题，可以考虑使用 “动态规划”：

1、定义 “状态”；
2、找到 “状态转移方程”。

记号说明： 下文中，使用记号 s[l, r] 表示原始字符串的一个子串，l、r 分别是区间的左右边界的索引值，使用左闭、右闭区间表示左右边界可以取到。举个例子，当 s = 'babad' 时，s[0, 1] = 'ba' ，s[2, 4] = 'bad'。

1、定义 “状态”，这里 “状态”数组是二维数组。

dp[l][r] 表示子串 s[l, r]（包括区间左右端点）是否构成回文串，是一个二维布尔型数组。即如果子串 s[l, r] 是回文串，那么 dp[l][r] = true。

2、找到 “状态转移方程”。

首先，我们很清楚一个事实：

1、当子串只包含 11 个字符，它一定是回文子串；

2、当子串包含 2 个以上字符的时候：如果 s[l, r] 是一个回文串，例如 “abccba”，那么这个回文串两边各往里面收缩一个字符（如果可以的话）的子串 s[l + 1, r - 1] 也一定是回文串，即：如果 dp[l][r] == true 成立，一定有 dp[l + 1][r - 1] = true 成立。

根据这一点，我们可以知道，给出一个子串 s[l, r] ，如果 s[l] != s[r]，那么这个子串就一定不是回文串。如果 s[l] == s[r] 成立，就接着判断 s[l + 1] 与 s[r - 1]，这很像中心扩散法的逆方法。

事实上，当 s[l] == s[r] 成立的时候，dp[l][r] 的值由 dp[l + 1][r - l] 决定，这一点也不难思考：当左右边界字符串相等的时候，整个字符串是否是回文就完全由“原字符串去掉左右边界”的子串是否回文决定。但是这里还需要再多考虑一点点：“原字符串去掉左右边界”的子串的边界情况。

1、当原字符串的元素个数为 33 个的时候，如果左右边界相等，那么去掉它们以后，只剩下 11 个字符，它一定是回文串，故原字符串也一定是回文串；

2、当原字符串的元素个数为 22 个的时候，如果左右边界相等，那么去掉它们以后，只剩下 00 个字符，显然原字符串也一定是回文串。

把上面两点归纳一下，只要 s[l + 1, r - 1] 至少包含两个元素，就有必要继续做判断，否则直接根据左右边界是否相等就能得到原字符串的回文性。而“s[l + 1, r - 1] 至少包含两个元素”等价于 l + 1 < r - 1，整理得 l - r < -2，或者 r - l > 2。

综上，如果一个字符串的左右边界相等，以下二者之一成立即可：
1、去掉左右边界以后的字符串不构成区间，即“ s[l + 1, r - 1] 至少包含两个元素”的反面，即 l - r >= -2，或者 r - l <= 2；
2、去掉左右边界以后的字符串是回文串，具体说，它的回文性决定了原字符串的回文性。

于是整理成“状态转移方程”：

dp[l, r] = (s[l] == s[r] and (l - r >= -2 or dp[l + 1, r - 1]))
或者

dp[l, r] = (s[l] == s[r] and (r - l <= 2 or dp[l + 1, r - 1]))
'''


