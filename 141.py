# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        node: ListNode = head

        while node != None:
            if node in visited:
                return True
            visited.add(node)
            node = node.next

        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while not fast is None and not fast.next is None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
