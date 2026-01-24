# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = -1
        while temp:
            count+=1
            temp = temp.next
        count = count / 2
        count = math.ceil(count)

        if count == 0:
            return None
        
        temp = head
        i = 0
        while temp:
            if i == count-1:
                break
            i+=1
            temp = temp.next

        temp.next = temp.next.next
        return head
        