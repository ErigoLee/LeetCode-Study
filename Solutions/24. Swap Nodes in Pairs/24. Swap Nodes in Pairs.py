# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        new_head = None
        current = None
        prev = None
        while head != None:
            first = head
            second = head.next
            if second == None and first != None:
                if prev != None:
                    prev.next = first
                else:
                    new_head = first
                break
            
            # second != None & first != None
            head = head.next.next
            current = ListNode(second.val)
            if prev != None:
                prev.next = current

            prev = current
            if new_head == None:
                new_head = current
            current = ListNode(first.val)
            prev.next = current
            prev = current

        return new_head 

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
new_node = Solution().swapPairs(node)
while new_node != None:
    print(new_node.val)
    new_node = new_node.next
