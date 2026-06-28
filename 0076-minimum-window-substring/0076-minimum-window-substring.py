from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_freq = Counter(t)
        window_freq = {}
        min_len= float('inf')
        substring_index = (-1, -1)
        left = 0
        required = len(need_freq)
        formed = 0
        for right in range(len(s)):
            curr_char = s[right]
            window_freq[curr_char] = window_freq.get(curr_char, 0) + 1
            if curr_char in need_freq and window_freq[curr_char] == need_freq[curr_char]:
                formed += 1
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    substring_index = (left, right)
                left_char = s[left]
                window_freq[left_char] -= 1
                if left_char in need_freq and window_freq[left_char] < need_freq[left_char]:
                    formed -= 1
                left += 1
        return "" if min_len == float('inf') else s[substring_index[0]: substring_index[1] + 1]
