"""

Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.



"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        j = 0 
        tmp = head
        start = head

        while tmp and j < n:
            tmp = tmp.next
            j += 1
        
        if not tmp:
            return head.next
        
        while tmp.next:
            tmp = tmp.next
            start = start.next
        start.next = start.next.next
        
        return head





