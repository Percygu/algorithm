'''
二叉树穿件和遍历
'''

#定义二叉树节点
class node(object):
    def __init__(self,value=None,lchild=None,rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class solution(object):
    #先序递归创建二叉树---创建当前节点
    def createTree(self,root,list):
        value = input("input a value\n")
        if value is not '#':
            root = node(value)
            list.append(root)
            root.lchild = self.createTree(root.lchild,list)
            root.rchild = self.createTree(root.rchild,list)
        else:
            roor = None
        return root

class solution1(object):
    def createTree(self):
        a,b,c,d,e,f = node('a'),node('b'),node('c'),node('d'),node('e'),node('f')
        a.lchild,a.rchild = b,e
        b.lchild,b.rchild = c,d
        e.lchild = f
        return a
    
    #先序遍历
    def Preorder(self,root):
        if root == None:
            return
        else:
            print(root.value,end='')
            self.Preorder(root.lchild)
            self.Preorder(root.rchild)

    #中序遍历
    def Inorder(self,root):
        if root == None:
            return
        else:
            self.Inorder(root.lchild)      #找到左孩子为空，则说明没有了左子树，他就是最左节点，是叶子节点，将其打印，再找右孩子节点
            print(root.value,end='')
            self.Inorder(root.rchild)
   
    #后序遍历
    def Postorder(self,root):
        if root == None:
            return
        else:
            self.Postorder(root.lchild)   
            self.Postorder(root.rchild)
            print(root.value,end='')

if __name__ == "__main__":
    s1 = solution1()
    root = s1.createTree()
    s1.Preorder(root)
    print()
    s1.Inorder(root)
    print()
    s1.Postorder(root)
    print()

