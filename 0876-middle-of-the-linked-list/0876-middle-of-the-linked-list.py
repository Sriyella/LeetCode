# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        a = 0
        dup = head

        while dup:
            #print(i, a, (i+1)//2)
            if (i+1)//2 >= a:
                out = head
                head = head.next
                a += 1
                
            dup = dup.next
            i += 1
                
            
        return out
            
        