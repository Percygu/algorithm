class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res,queue = [],[]
        if not root:
            return queue
        p = root
        print(queue)
        queue.append(p.val)
        while queue:
            values = []
                for p in queue:               #遍历当前层的时候，把下一层需要遍历的节点加入到队列
                values.append(p.val)          #遍历当前节点
                if p.left:
                    queue.append(p.left)      #当前节点的左孩子加入到队列
                if p.right:
                    queue.append(p,right)     #当前节点的右孩子加入到队列
                queue.pop(p)                  #当前节点出队列
                res.append(values)            #value接入到最终数组
        return res