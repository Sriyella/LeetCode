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
        i = 0
        while head.next:
            head = head.next
            #print('-', head)
            out2 = ListNode(val=head.val)
            #print('--', out2, head)
            out2.next = out
            out = out2
            #print('---', out, out2, head)
            i += 1
        return out