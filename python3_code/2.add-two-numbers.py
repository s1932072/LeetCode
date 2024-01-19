#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


'''
行いたいこと
l1,l2の内容について、まず取得をする。
で、同じリストの位置にあるもの同士を計算して、10で割る
その係数について、は別途保持して、次に計算に使用する


'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cureent = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            cureent.next = ListNode(total % 10)

            cureent = cureent.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        