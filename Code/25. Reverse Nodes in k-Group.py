# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        lst = []
        count = k
        while head:
            lst.append(head)
            head = head.next
            count -= 1
            if count == 0:
                break
        if count > 0: # not enough nodes to flip
            return lst[0]
        lst[0].next = lst[-1].next
        for i in range(len(lst) - 1, 0, -1):
            lst[i].next = lst[i - 1]
        lst[0].next = self.reverseKGroup(lst[0].next, k)
        return lst[-1]