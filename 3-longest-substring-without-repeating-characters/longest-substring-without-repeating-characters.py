class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {}
        max_length = 0
        start = 0
        for i, char in enumerate(s):
            if char in char_dict and char_dict[char] >= start:
                start = char_dict[char] + 1
            char_dict[char] = i
            max_length = max(max_length, i - start + 1)
        return max_length