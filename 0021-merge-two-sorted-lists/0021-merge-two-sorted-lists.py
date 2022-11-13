# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode(val=None)
        out2 = out
        while True:
            if list1 != None and list2 != None:
                if list1.val != None and list2.val != None:
                    if list1.val > list2.val:
                        out.val = list2.val
                        if list2.next != None:
                            list2 = list2.next
                        else:
                            out.next = list1
                            break
                    else:
                        out.val = list1.val
                        if list1.next != None:
                            list1 = list1.next
                        else:
                            out.next = list2
                            break
                elif list1.val != None:
                    out = list1
                    break
                elif list2.val != None:
                    out = list2
                    break
                else:
                    break
                out.next = ListNode()
                out = out.next
            elif list2 != None:
                out.val = list2.val
                out.next = list2.next
                break
            elif list1 != None:
                out2.val = list1.val
                out2.next = list1.next
                break
            else:
                break

        if out2.val==None:
            out2 = None
        return out2




        