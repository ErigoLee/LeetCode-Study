# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        head = None
        current = None
        prev = None
        value = 10001

        while True:
            finished = True
            for i in lists:
                if i != None:
                    finished = False
                    break
            
            if finished == True:
                break
            
            move_index = -1
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                if value > lists[i].val:
                    value = lists[i].val
                    move_index = i
            
            if move_index <= -1:
                return None
            else:
                current = ListNode()
                current.val = value
                lists[move_index] = lists[move_index].next
            
            if head == None:
                head = current
            if prev != None:
                prev.next = current
            
            prev=current
            value = 10001
        return head

l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))

result = Solution().mergeKLists([l1, l2, l3])

while result:
    print(result.val, end=" -> ")
    result = result.next