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

class solution(object):
     def diameterOfBinaryTree(self, root):
        res = 0
        d = []
        d =  self.dfs(root,res,d)
        print(d)
        if not d:
            return 0
        return max(d)


    #递归求各个最高点的路径
    def dfs(self,root,res,d):
        #先序遍历二叉树中的各个点，把各个点作为最高点求左右子树深度和
        if not root:
            return 0
        else:
           # print("root.val=",root.val,d)
            deepth = self.getTreeDeep(root.left) +  self.getTreeDeep(root.right)  #求遍历到的当前节点左右子树的深度之和  
            d.append(deepth)
           #print("root.deepth=",deepth)
            res = max(res,deepth)
           # print("res=",res)
            self.dfs(root.left,res,d)
            self.dfs(root.right,res,d)
        return d
      
    #获取二叉树的深度
    def getTreeDeep(self,root):
        if not root:
            return 0
        left = self.getTreeDeep(root.left)        #左子树深度
        right = self.getTreeDeep(root.right)      #右子树深度
        
        return left+1 if left>right else right+1     #返回左子树和右子树深度中较大的一个加一为整棵树的深度