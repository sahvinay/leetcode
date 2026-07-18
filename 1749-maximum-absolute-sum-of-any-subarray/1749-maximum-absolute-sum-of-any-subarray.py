class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_ending = 0
        min_ending = 0
        result = 0

        for num in nums:
            max_ending = max(num, max_ending + num)
            min_ending = min(num, min_ending + num)

            result = max(
                result,
                abs(max_ending),
                abs(min_ending)
            )

        return result