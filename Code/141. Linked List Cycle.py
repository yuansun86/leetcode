# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        if not slow or not slow.next:
            return False
        fast = head.next
        while fast.next and fast.next.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False