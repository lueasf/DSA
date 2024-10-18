# Add two numbers : Amazon

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# BYME
class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        carry = 0 # la retenue
        curr = head
        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            tot = l1_val + l2_val + carry
            curr.next = ListNode(tot % 10)
            carry = tot // 10 # ce sera 0 ou 1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return head.next
        