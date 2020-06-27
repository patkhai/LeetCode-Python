'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

'''


class Solution(object):
    @staticmethod
    def swapNodes(head):
        if not head or not head.next:
            return head

        dummy = Node(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            Solution.swapPairs(curr)        
            curr = curr.next.next
        return dummy.next
    
    @staticmethod
    def swapPairs(curr): 
        first = curr.next
        second = curr.next.next

        curr.next = second
        first.next = second.next
        second.next = first
        
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} > {self.next}"


listNode = Node(1)
listNode.next = Node(4)
listNode.next.next = Node(2)
listNode.next.next.next = Node(3)
print(listNode)
newlist = Solution.swapNodes(listNode)
print(newlist)

