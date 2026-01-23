# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        count = 0
        temp = head
        while temp:
            if count%2==0:
                odd.append(temp.val)
            elif count%2!=0:
                even.append(temp.val)
            temp = temp.next
            count+=1
        
        temp = head
        i = 0
        j = 0
        while temp:
            if i <= len(odd)-1:
                temp.val = odd[i]
                i+=1
            else:
                temp.val = even[j]
                j+=1
            temp = temp.next
        return head








        