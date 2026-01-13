# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def count_dp(self, node, idx):
        if node == None:
            return idx
        else:
            idx = idx + 1
            return self.count_dp(node.next, idx)

    def remove(self, head, n):
        total_count = self.count_dp(head,0)
        remove_idx = total_count - n
        idx = 0
        prev = head
        current = head
        next_node = head.next
        while remove_idx <= total_count:
            if remove_idx == idx:
                if current == head:
                    head = next_node
                else:
                    prev.next = next_node
                break
            prev = current
            current = current.next
            if current == None:
                next_node = None
            else:
                next_node = current.next
            idx = idx + 1
        return head


    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        head = self.remove(head, n)

        return head

head = ListNode(5,ListNode(4,ListNode(3,ListNode(2,ListNode(1)))))
head2 = Solution().removeNthFromEnd(head,2)

print(head2.val)
print(head2.next.val)
print(head2.next.next.val)
print(head2.next.next.next.val)