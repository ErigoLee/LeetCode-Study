# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k <= 1:
            return head
    
        new_head = None
        prev = None
        current = None

        while head != None:
            stack = []
            notCompleted = False
            for _ in range(k):
                if head == None:
                    notCompleted = True
                    break
                stack.append(head)
                head = head.next        
            
            if notCompleted == True:
                if current == None:
                    return head
                else:
                    current.next = stack[0]
                    break
            
            while len(stack) > 0:
                current = ListNode(stack.pop().val)
                if new_head == None:
                    new_head = current
                if prev != None:
                    prev.next = current
                prev = current
        
        return new_head
    
node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_node = Solution().reverseKGroup(node, 2)
while new_node != None:
    print(new_node.val)
    new_node = new_node.next
        