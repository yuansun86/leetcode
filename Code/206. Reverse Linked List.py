# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow = None
        fast, temp = head, head
        while fast.next:
            fast = fast.next
            temp.next = slow
            slow = temp
            temp = fast
        fast.next = slow
        return fast