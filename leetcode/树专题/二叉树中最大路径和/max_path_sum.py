'''
1.枚举所有最高点（每条路径都有一个最高点）
2.对每个最高点求其左子树和其有字数的深度之和
3.取深度之和的最大值
'''

class TreeNode:              #空节点也认为是BST
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root: TreeNode) -> int:
        res = [float('-inf')]                             #用数组传递，改变值本身，避免值传递,初始化为负无穷
        self.dfs(root,res)
        return res[0]

    def dfs(self,root,res):                          #返当前节点的带权最大深度
        if not root:
            return 0
        left = max(0,self.dfs(root.left,res))        #递归求左孩子的带权最大深度,如果左孩子小于0，则不加
        right = max(0,self.dfs(root.right,res))      #递归求右孩子的带权最大深度，如果右孩子小于0，则不加
        res[0] = max(res[0],root.val+left+right)     #此时root为最高点，所以最大带权路径为root.val+dfs(root.left)+dfs(root.right)
        #三种情况，要么往左子树走，要么望往右子树走，要么不走
        return root.val+max(left,right)      #最高点root的带权深度,这个返回主要用于root的父节点来求深度的时候用

   