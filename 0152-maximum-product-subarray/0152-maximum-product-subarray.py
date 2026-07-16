class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_sum = nums[0]
        max_sum = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = min_sum * nums[i]
            v3 = max_sum * nums[i]
            min_sum = min(v1, v2, v3)
            max_sum = max(v1, v2, v3)
            ans = max(ans, min_sum, max_sum)
        return ans
