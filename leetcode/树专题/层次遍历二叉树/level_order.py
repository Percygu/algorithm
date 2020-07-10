'''
采用一个队列来记录接下来要遍历的下一层的节点，在当前层开始遍历的时候，就可以求出所有节点的左右孩子
把所有孩子放入到队列中座位下一层遍历的节点
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def levelOrder(self,root):
        if not root:
            return []
        levels = []            #用来记录最终结果
        next_level = []        #下一层待遍历的点
        next_level.append(root)    #首先遍里根节点,转移none也可以作为一个元素加入到next_level中
        while next_level:          #队列里还有当前层的节点
            n = len(next_level)    #求出队列里当前遍历的节点个数
            values = []
            for i in range(n):       #for循环结束后，当前层的所有节点的值都会加入到values中，当前层的所有节点都将从next_level删掉，而在next_level加入所有下一层将要遍历的节点
                p = next_level[i]
                values.append(p.val)   #把当前层的值记录下来
                if p.left:             #左孩子不为空，把左孩子加入到代币哪里队列
                    next_level.append(p.left)
                if p.right:            #右孩子不为空，把右孩子加入到代币哪里队列
                    next_level.append(p.right)
            del next_level[:n]         #删除遍历过的当前层的节点
            levels.append(values)
        return levels  
            
                    




        
        