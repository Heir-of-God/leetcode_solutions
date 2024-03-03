# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        n_nodes = 0
        temp: list[ListNode] = []

        node: ListNode = head
        while node:
            temp.append(node)
            node = node.next
            n_nodes += 1

        if n == n_nodes:
            return temp[1]
        elif n == 1:
            temp[-2].next = None
            return head
        else:
            del_ind: int = n_nodes - n
            temp[del_ind - 1].next = temp[del_ind + 1]
            return head


# First solution with using extra space


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast: ListNode = head
        slow: ListNode = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
