class TreeNode:              #空节点也认为是BST
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 区间法------因为BST左孩子总是小于父节点，右孩子总是大于父节点，则从根节点开始，递归找到各个子节点，看各个子节点的取值是否在正确的区间内
class solution1(object):
    def isValidBST(self, root):
        if root == None:
            return False
        return self.dfs(root,float('-inf'),float('inf'))        #初始化根节点的上下限为负无穷和正无穷
        
    def dfs(self,root,min_val,max_val):                         #left为当前节点的取值下限，right为当前节点的取值上线,入参：节点和区间
        if not root:
            return True                                        #递归直到遍历到当前节点为空，即都是满足区间条件的，所以返回true。
        if root.val < min_val or root.val > max_val:
            return False
        #递归，做孩子的取值下限为min_val，上限为root.val-1,右孩子取值下限为root.val+1,上限为max_val
        return self.dfs(root.left,min_val,root.val-1) and self.dfs(root.right,root.val+1,max_val)  


#  中序遍历记录所有的节点到list，看list是否是单调递增即可
class solution2(object):
    def isValidBST(self,root):              
        values = []
        values = self.inorderdfs(root,values)
        print(values)
        for i in range(len(values)-1):
            if values[i+1] <= values[i]:
                return False
        return True
        

    def inorderdfs(self,root,values):
        #中序遍历，把节点的value记录到list中
        if not root:
            return values
        else:
            self.inorderdfs(root.left,values)      #继续找左孩子
            values.append(root.val)
            self.inorderdfs(root.right,values)
        return values

if __name__ == "__main__":
    a,b,c,d,e = TreeNode(5),TreeNode(1),TreeNode(4),TreeNode(3),TreeNode(6)
    a.left = b
    a.right = c
    c.left = d
    c.right = e

    s1 = solution1()
    s2 = solution2()
    print(s1.isValidBST(a))
    print(s2.isValidBST(a))





        


    

