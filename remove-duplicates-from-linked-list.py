class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        while tmp:
            while tmp.next and tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            tmp = tmp.next
        return head

