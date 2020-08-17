
class Solution:
    def mergeTwoLists(self,  l1: ListNode, l2: ListNode) -> ListNode:
        l3 = curr = ListNode()
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1 is not None:
            curr.next = l1
        elif l2 is not None:
            curr.next = l2
            
            
        return l3.next

            
