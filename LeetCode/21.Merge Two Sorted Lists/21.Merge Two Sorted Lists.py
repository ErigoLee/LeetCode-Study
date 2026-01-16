class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None
        current = head
        prev = current

        while True:
            if list1 == None and list2 == None:
                break
            elif list1 == None:
                current = ListNode()
                current.val = list2.val
                list2 = list2.next
            elif list2 == None:
                current = ListNode()
                current.val = list1.val
                list1 = list1.next
            else:
                current = ListNode()    
                if list1.val <= list2.val:
                    current.val = list1.val
                    list1 = list1.next
                else:
                    current.val = list2.val
                    list2 = list2.next
            if head == None:
                head = current
            if prev != None:
                prev.next = current
            prev = current
        return head

list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
checked_node = Solution().mergeTwoLists(list1, list2)

while checked_node != None:
    print(checked_node.val)
    checked_node = checked_node.next

