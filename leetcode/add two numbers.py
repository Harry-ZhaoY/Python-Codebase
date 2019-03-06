# add two numbers
'''
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        current = l3
        carry = 0
        while l1 or l2: 
            if l1 is None:
                l1v = 0
            else:
                l1v = l1.val
            if l2 is None:
                l2v = 0
            else:
                l2v = l2.val
            # Sum
            tmp = l1v + l2v + carry
            if tmp >= 10:
                x = tmp%10
                carry = int(tmp/10)
            else:
                x = tmp
                carry = 0
            # Assign value
            current.next = ListNode(x)
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry != 0:
            current.next = ListNode(carry)
        return l3.next