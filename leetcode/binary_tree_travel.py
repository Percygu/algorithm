'''
二叉树及遍历
            1
        2        6
    3     4    7   
            5     8
'''

#定义二叉树节点
class Node(object):
    def __init__(self,val):   #构造函数
        self.val = val #节点值
        self.lchild,self.rchild = None,None  #初始化左右孩子为none

#先序遍历------根左右
class PreSolution:
    def preTraversal(self,root):
        if root == None:
            return []
        stack = []   #记录访问节点
        seq = []     #记录访问节点的值，即遍历每个节点
        while (root != None) | (len(stack) != 0):
            if root != None:
                seq.append(root.val)      #直接访问该节点的值，完成当前节点的遍历
                stack.append(root)        #将当前节点加入到队列中，以便后续回溯
                root = root.lchild        #向左孩子走
            else:
                root = stack.pop()        #此时是当前遍历子树的根节点，已经访问过，所以接下来访问其右孩子
                root = root.rchild
        return seq

#中序遍历-----左根右
class InSolution:
    def inTravsal(self,root):
        if root == None:
            return []
        stack = []
        seq = []
        while (root != None) | (len(stack) !=0):
            if root != None:
                stack.append(root)    #将当前节点加入到队列中，以便后续回溯
                root = root.lchild
            else:
                root = stack.pop()    #此时是当前遍历子树的根节点，还没被访问，直接访问
                seq.append(root.val)
                root = root.rchild
        return seq


#后序遍历-----左右根---可认为左右根是根右左的反序列，根右左在先序遍历的基础上稍作改动即可
class PostSolution:
    def postTravsal(self,root):
        if root == None:
            return []
        seq = []
        stack = []
        result = []
        while (root != None) | (len(stack) != 0):
            if root != None:
                seq.append(root.val)
                stack.append(root)
                root = root.rchild   #这里跟先序序列相反
            else:
                root = stack.pop()
                root = root.lchild
        while seq:
            result.append(seq.pop())
        return result


if __name__ == "__main__":
    b1 = Node(1)
    b2 = Node(2)
    b3 = Node(3)
    b4 = Node(4)
    b5 = Node(5)
    b6 = Node(6)
    b7 = Node(7)
    b8 = Node(8)
    b1.lchild = b2
    b2.lchild = b3
    b2.rchild = b4
    b4.rchild = b5
    b1.rchild = b6
    b6.lchild = b7
    b7.rchild = b8
    s1 = PreSolution()
    s2 = InSolution()
    s3 = PostSolution()
    print(s1.preTraversal(b1))
    print(s2.inTravsal(b1))
    print(s3.postTravsal(b1))