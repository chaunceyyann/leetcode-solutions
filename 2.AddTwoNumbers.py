# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        head=l1
        while l2:
            tmp=l1.val+l2.val+carry
            l1.val=tmp%10
            carry = 1 if tmp//10!=0 else 0
            if not l2.next and carry==0:
                break
            if not l1.next:
                l1.next=ListNode(0)
            if not l2.next:
                l2.next=ListNode(0)

            l1=l1.next
            l2=l2.next

        return head
