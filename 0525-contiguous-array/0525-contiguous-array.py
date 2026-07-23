class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_index = {0: -1}

        current_sum = 0
        max_length = 0

        for i, num in enumerate(nums):
            if num == 0:
                current_sum -= 1
            else:
                current_sum += 1

            if current_sum in prefix_index:
                length = i - prefix_index[current_sum]
                max_length = max(max_length, length)
            else:
                prefix_index[current_sum] = i

        return max_length