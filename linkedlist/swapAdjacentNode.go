package linkedlist

/*
****交换链表的相邻两个元素
1-2-3-4-5-6  ------->  2-1-4-3-6-5
*/

type Node struct {
	val  int
	next *Node
}

//交换链表的相邻两个元素
func swapAdjacentNode(head *Node) *Node {
	root := new(Node)
	root.next = head         //创建一个头结点指向第一个节点
	var current *Node = root //复制当前链表,使当前节点current也指向第一个节点
	for current.next != nil && current.next.next != nil {
		first := current.next       //first=1->2,
		second := current.next.next //second=2->3
		first.next = second.next    //first->3:  要交换1，2的位置，因为链表只有一个后继指针，所以要保存后一个节点2的next，将1指向3，即
		current.next = first.next   //current->2
		second.next = first
		current.next = second
		current = current.next.next
	}
	return root.next
}

func main() {

}
