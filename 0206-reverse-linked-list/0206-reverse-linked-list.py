# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            out = ListNode(val=head.val)
        else:
            return None
        
        while head.next:
            head = head.next
            out2 = ListNode(val=head.val)
            out2.next = out
            out = out2

        return out