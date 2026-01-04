class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    conveyNum = 0
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        if l1 is not None and l2 is not None:
            result.val = l1.val + l2.val + self.conveyNum
            if result.val > 9:
                self.conveyNum = int(result.val / 10)
                result.val = int(result.val % 10)
            else:
                self.conveyNum = 0

        if l1 is not None and l2 is None:
            result.val = l1.val + self.conveyNum
            if result.val > 9:
                self.conveyNum = int(result.val / 10)
                result.val = int(result.val % 10)
            else:
                self.conveyNum = 0

        if l2 is not None and l1 is None:
            result.val = l2.val + self.conveyNum
            if result.val > 9:
                self.conveyNum = int(result.val % 10)
                result.val = int(result.val % 10)
            else:
                self.conveyNum = 0

        if l1.next is not None and l2.next is not None:
            result.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            if l1.next is None and l2.next is None:
                if self.conveyNum == 0:
                    result.next = None
                else:
                    result.next = ListNode(self.conveyNum,None)
            else:
                if l1.next is None:
                    result.next = self.addTwoNumbers(ListNode(), l2.next)
                else:
                    result.next = self.addTwoNumbers(l1.next, ListNode())
        return result