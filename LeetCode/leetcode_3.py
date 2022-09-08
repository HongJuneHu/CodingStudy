class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = {}
        start = 0
        longest = 0
        for i, value in enumerate(s):
            if value in hash_table and hash_table[value] >= start:
                start = hash_table[value] + 1
            else:
                hash_table[value] = i
            hash_table[value] = i
            longest = max(longest, len(s[start: i + 1]))
        return longest