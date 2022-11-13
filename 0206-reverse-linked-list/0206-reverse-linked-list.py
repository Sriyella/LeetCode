# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = None
        
        while head:
            out2 = ListNode(val=head.val)
            head = head.next
            out2.next = out
            out = out2

        return out