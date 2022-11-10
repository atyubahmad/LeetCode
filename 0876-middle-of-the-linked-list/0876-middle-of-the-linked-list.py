# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head
        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next
        
        return prev