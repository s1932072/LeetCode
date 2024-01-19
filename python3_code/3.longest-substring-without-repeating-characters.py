#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chat_dict = {}
        start = 0
        max_length = 0

        for end in range (len(s)):
            if s[end] in chat_dict and chat_dict[s[end]] >= start:
                start = chat_dict[s[end]] + 1

            chat_dict[s[end]] = end 

            max_length = max(max_length, end - start + 1)

        return max_length
# @lc code=end

