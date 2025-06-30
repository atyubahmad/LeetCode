# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        arr  = []
        while curr:
            if curr.val not in arr:
                arr.append(curr.val)
                
            curr = curr.next 

        if not arr:
            return None

        new_head = ListNode(arr[0])
        temp = new_head
        
        for i in range(1, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        
        return new_head