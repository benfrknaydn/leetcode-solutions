# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pointer=ListNode(-1)
        temp = pointer 
        overflow=0
        while l1 or l2 or overflow:
            total = (l1.val if l1 else 0) +(l2.val if l2 else 0) + overflow 
            temp.next = ListNode(total % 10)
            overflow = total // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            temp = temp.next
        return pointer.next