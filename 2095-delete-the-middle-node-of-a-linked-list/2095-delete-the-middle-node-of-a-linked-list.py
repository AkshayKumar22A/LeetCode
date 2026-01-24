# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge Case: If list has only 1 node, delete it and return None
        if not head.next:
            return None
            
        slow = head
        fast = head.next.next # Start fast 2 steps ahead!
        
        # Why start fast at head.next.next?
        # We want 'slow' to stop ONE STEP BEFORE the middle.
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Now 'slow' is exactly behind the middle node.
        # Skip the middle node:
        slow.next = slow.next.next
        
        return head

        