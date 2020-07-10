'''
通过栈来实现
1.如果节点有左孩子，则不停地把左孩子压入栈中，直到左孩子为空
2.取出栈顶元素，输出，再把右孩子节点压入栈中
3.重复上述两步
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution(object):
    def inorderTraversal(self,root):
        stack = []
        res = []
        p = root
        while (p or stack):            # 终止条件：节点不为空或者栈不为空
            while (p):                 #1.首先将当前节点压入栈中，如果节点有左孩子，则不停地把左孩子压入栈中，直到左孩子为空         
                stack.append(p)
                p = p.left
            p = stack.pop()            #2.取出栈顶元素输出
            res.append(p.val)
            p = p.right                #3.右孩子节点入栈
        return res 

if __name__ == "__main__":
    a,b,c,d,e,f = TreeNode('a'),TreeNode('b'),TreeNode('c'),TreeNode('d'),TreeNode('e'),TreeNode('f')
    a.left,a.right = b,e
    b.left,b.right = c,d
    e.left = f
    s = solution()
    print(s.inorderTraversal(a))

            
            
        