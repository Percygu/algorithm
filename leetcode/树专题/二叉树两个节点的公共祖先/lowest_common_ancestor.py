'''
1.根节点是p或q中的一个，则返回根节点
2.p,q都在左子树或者右子树中，则p，q的最近公共祖先去左右子树中递归查找
3.p,q一个在左子树，一个在右子树中，则根节点就是最近公共祖先
'''

class TreeNode:              #空节点也认为是BST
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def lowestCommonAncestor(self,root,p,q):
        if p == root or q == root or not root:   #如果根节点是p或q中的一个，则返回根节点
            return root 
    
        left = self.lowestCommonAncestor(root.left,p,q)     #在左子树中查找
        right = self.lowestCommonAncestor(root.right,p,q)   #在右子树中查找

        if not left:                                        #左子树中返回空，说明最近公共祖先在右子树中，p，q都在右子树
            return right
        if not right:                                       #右子树中返回空，说明最近公共祖先在左子树中，p，q都在左子树
            return left
    
        return root                                         #p，q既不都在左子树，也不都在右子树，说明分开在左右子树中，根节点就是为最近公共祖先


        
