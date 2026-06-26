# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ## LINKED LIST | time: O(n), space: O(1)
        # slow pointer moves 1, fast pointer moves 2
        # if cycle, fast poiner will eventually meet slow poitner
        # if no cycle, fast pointer will reach null

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False
        