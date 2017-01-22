# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        rtn = ListNode(0)
        if l1 != None or l2 != None:
            if l1 != None:
                sum = l1.val
            if l2 != None:
                sum = l2.val
            if l1 != None and l2 != None:
                sum = l1.val + l2.val
                print sum
                if sum > 9:
                    rtn.next = ListNode(1)
                else :
                    rtn.next = ListNode(0)
                rtn.val += sum%10
            rtn.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            
            return rtn
