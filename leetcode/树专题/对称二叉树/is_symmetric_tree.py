'''
1.左右两棵树的根节点相等
2.左根节点的左子树等于右根节点的右子树
3.左根节点的右子树等于右根节点的左子树
'''

class TreeNode:              #空节点也认为是BST
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归方式
class solution1(object):
    def isSymmetric(self,root):
        if not root:                         #空树是特殊的对称二叉树
            return True
        return self.dfs(root.lsft,root.right)
    

    def dfs(p,q):
        if not p or not q:                   #两个子树的根节点存在空的情况
            return ((not p) and (not q))     #判断两个子树是否都为空即可，若都为空则对称，返回true。不都为空，则不对称，返回false
        return (p.val == q.val) and self.dfs(p.left,q.right) and self.dfs(p.right,q.left)


'''
根据中序遍历的迭代方法，同时遍历左子树和右子树
左子树：左-根-右
右子树：右-根-左
'''
#迭代方法 
class solution2(object):
    def isSymmetric(self,root):
        if not root:
            return True
        p,q = root.left,root.right
        stack_p = []
        stack_q = []
        while(p or q or stack_p or stack_q):
            while(p and q):                       #同时往边上寻找，有一个为空则停止
                stack_p.append(p)                 #p,q同时入栈
                stack_q.append(q)
                p,q = p.left,q.right
            if (p or q):                          #一个为空，一个不为空，显然不对称
                return False
            print(stack_p)
            print(stack_q)
            p = stack_p.pop()                     #stack_p栈顶出栈       
            q = stack_q.pop()                     #stack_q栈顶出栈
            if p.val != q.val:
                return False
            p,q = p.right,q.left                  #左根节点的右孩子入栈，右根节点的左孩子入栈
        return True

if __name__ == "__main__":
    a,b,c,d,e,f,g = TreeNode(1),TreeNode(2),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(4),TreeNode(3)
    a.left,a.right = b,c
    b.left,b.right = d,e
    c.left,c.right = f,g

    s2 = solution2()
    print(s2.isSymmetric(a))




    

    
        
