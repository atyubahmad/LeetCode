# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return head

        odd = head
        even = None
        last = None
        head2 = None

        while(odd.next != None):
            even = odd.next
            odd.next = even.next
            even.next = None
            if (head2 is None):
                head2 = even
                last = even
            else:
                last.next = even
                last = even
            if(odd.next != None):
                odd = odd.next


        odd.next = head2
        return head