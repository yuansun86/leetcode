# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    tail = None
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        sentinel = ListNode()
        sentinel.next = head
        if not head:
            return None
        if not head.next or not head.next.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left = slow
        right = slow.next
        self.reverse(right)
        left.next = None
        right.next = None
        tail = self.tail
        while head.next:
            next_node = head.next
            head.next = tail
            head = tail
            tail = next_node
        head.next = tail
        return sentinel.next
        
        
        
    def reverse(self, node):
        if not node.next:
            self.tail = node
            return node
        right = self.reverse(node.next)
        right.next = node
        return node
        