# Solution version: 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isHappy(self, n: int) -> bool:
        def square_digit(num: int) -> int:
            square_num = 0
            while num:
                digit = num % 10
                square_num += digit * digit
                num //= 10
            return square_num

        slow = n
        fast = n

        while True:
            slow = square_digit(slow)
            fast = square_digit(square_digit(fast))

            if slow == fast:
                return slow == 1
