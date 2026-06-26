# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ## LINKED LIST | time: O(n), space: O(1)
        # use dummy pointer since head can be removed
        # left pointer starts dummy, right poiner starts head
        # move right pointer n steps ahead
        # move both pointers together until right pointer reaches end
        # left pointer right before node to be removed

        # handle deletion of first node
        dummy = ListNode(0, head)   
        
        # move right pointer n times
        left, right = dummy, head
        for _ in range(n):
            right = right.next
        
        # move both pointers until right reaches end
        while right:
            left = left.next
            right = right.next
        
        # delete node
        left.next = left.next.next

        # return updated head
        return dummy.next
        