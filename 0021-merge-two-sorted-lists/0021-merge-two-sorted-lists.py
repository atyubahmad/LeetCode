# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        curr1 = list1
        curr2 = list2
        
        array = []

        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                array.append(curr1.val)
                curr1 = curr1.next
            else:
                array.append(curr2.val)
                curr2 = curr2.next

        
        while curr1 is not None:
            array.append(curr1.val)
            curr1 = curr1.next

        while curr2 is not None:
            array.append(curr2.val)
            curr2 = curr2.next

        
        if not array:  
            return None
        
        newList = ListNode(array[0])
        temp = newList
        
        
        for i in range(1, len(array)):
            temp.next = ListNode(array[i])  
            temp = temp.next  
        
        return newList