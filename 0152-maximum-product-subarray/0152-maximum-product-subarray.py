class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for num in nums[1:]:
            prev_max = current_max
            prev_min = current_min

            current_max = max(
                num,
                prev_max * num,
                prev_min * num
            )

            current_min = min(
                num,
                prev_max * num,
                prev_min * num
            )

            result = max(result, current_max)

        return result