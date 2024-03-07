# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer: ListNode = head
        fast_pointer: ListNode = head

        while fast_pointer != None:
            fast_pointer = fast_pointer.next
            if fast_pointer:
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next

        return slow_pointer
