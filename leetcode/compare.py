if len(self.hashmap) == self.capacity:
            #删除队首节点
            self.hashmap.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        #创建新节点
        node = Node(key,value)
        self.hashmap[key] = node
        #队尾插入新节点
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node       
        self.tail.perv = node


            
            

            




