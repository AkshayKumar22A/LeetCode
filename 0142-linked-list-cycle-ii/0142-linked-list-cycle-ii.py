# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        temp = head
        while temp:
            visited.add(temp)
            temp = temp.next
            if temp in visited:
                return temp
        return None
        