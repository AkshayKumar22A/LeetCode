# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length+=1
            temp = temp.next
        
        if length == n:
            new_head = head.next
            return new_head
        
        remove = length - n
        temp = head

        while temp is not None:
            remove -= 1
            if remove == 0:
                break
            temp = temp.next

        # Remove the nth node from the end
        temp.next = temp.next.next

        return head