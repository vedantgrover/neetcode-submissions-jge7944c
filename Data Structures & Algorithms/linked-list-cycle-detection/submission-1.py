# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        curr = head
        f = head

        while f != None and f.next != None:
            curr = curr.next
            f = f.next.next

            if curr == f:
                return True

        return False
            