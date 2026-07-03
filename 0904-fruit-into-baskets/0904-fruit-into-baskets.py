class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = 0
        freq = {}
        # [3,3,3,1,2,1,1,2,3,3,4]
        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            count = max(count, right - left + 1)
        return count