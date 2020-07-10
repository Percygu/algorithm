'''
1.通过前序遍历找到每次的根节点的长度
2.通过中序遍历找到左右子树的长度
3.在递归先创建根节点，左子树，右子树
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def buildTree(self,preorder,inorder):      #preorder为先序遍历数组，inorder为中序遍历数组
        n = len(preorder)
        pos = {}
        for i in range(n):                     #中序遍历中，为了在o(1)时间内根据元素值找到其对应的位置，用一个map来存储
            pos[inorder[i]] = i
        return self.dfs(preorder,0,n-1,inorder,0,n-1,pos)

    def dfs(self,preorder,left_p,right_p,inorder,left_i,right_i,pos):   #每次根据一组对应的先序遍历和中序遍历区间创建出一个节点
        if right_p < left_p:                   #递归终止条件，right_p < left_p说明length=0，k=left_p，子树区间里长度为0，则左右自述均无法创建了，递归终止
            return None
        val = preorder[left_p]                 #p为根节点对应的值
        k = pos[val]                           #在中序遍历中找到根节点的位置
        length = k-left_i                      #确定左子树长度，这样就有了左子树和右子树区间，可以递归创建---递归创建过程一定是最后只会创建出一个节点
        root = TreeNode(val)                   #创建出根节点
        root.left = self.dfs(preorder,left_p+1,left_p+length,inorder,left_i,k-1,pos)
        root.right = self.dfs(preorder,left_p+length+1,right_p,inorder,k+1,right_i,pos)
        return root


        

