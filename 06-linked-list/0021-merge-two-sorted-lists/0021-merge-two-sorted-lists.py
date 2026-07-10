# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ## LINKED LIST | time: O(n + m), space: O(1)
        # keep pointer to head & end
        # choose smaller head node to add to end
        # move pointer forward until one list is empty
        # add remaining nodes from non-empty list
        dummy = ListNode()      # stores head
        temp = dummy            # iterate this

        # while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1   # add list1 to new list
                list1 = list1.next  # update list1
            else:
                temp.next = list2   # add list2 to new list
                list2 = list2.next  # update list2
            temp = temp.next        # update temp to next
        
        # add remaining nodes from non-empty list
        temp.next = list1 or list2

        return dummy.next
        