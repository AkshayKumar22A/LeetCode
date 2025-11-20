# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = None
        n = node
        itr = node.next
        while itr:
            n.val = itr.val
            itr = itr.next
            n = n.next
        
        i = node
        while i.next.next:
            i = i.next
        i.next = None
        