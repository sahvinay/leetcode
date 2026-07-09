class Solution:
    def isHappy(self, n: int) -> bool:
        def next_number(num):
            square_sum = 0

            while num > 0:
                digit = num % 10
                square_sum += digit * digit
                num //= 10

            return square_sum

        slow = n
        fast = next_number(n)

        while fast != 1 and slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return fast == 1