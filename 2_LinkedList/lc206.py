
# BYME
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        new_list = None
        curr = head

        while (curr):
            next_node = curr.next
            curr.next = new_list
            new_list = curr.next
            curr = next_node
        return new_list