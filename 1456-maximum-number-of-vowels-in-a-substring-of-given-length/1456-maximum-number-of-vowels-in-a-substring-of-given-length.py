class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        curr_count = 0

        # Count vowels in first window
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1

        max_count = curr_count

        # Slide the window
        for right in range(k, len(s)):
            left = right - k

            # Remove left character
            if s[left] in vowels:
                curr_count -= 1

            # Add right character
            if s[right] in vowels:
                curr_count += 1

            max_count = max(max_count, curr_count)

        return max_count