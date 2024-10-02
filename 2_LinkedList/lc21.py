
# BYME (avec des listes normales)
def merge(l1, l2):
    def aux(output, l1, l2, i, j):

        if i == len(l1) and j == len(l2):
            return output
        
        if i == len(l1):
            return output + l2[j:]
        if j == len(l2):
            return output + l1[i:]
        
        if l1[i] < l2[j]:
            output.append(l1[i])
            return aux(output, l1, l2, i + 1, j)
        elif l1[i] > l2[j]:
            output.append(l2[j])
            return aux(output, l1, l2, i, j + 1)
        else:
            output.append(l1[i])
            output.append(l2[j])
            return aux(output, l1, l2, i + 1, j + 1)

    return aux([], l1, l2, 0, 0)

# NOT BYME (avec des listes chainées)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else : 
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return head.next