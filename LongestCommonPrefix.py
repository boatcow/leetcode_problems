# 14. Longest Common Prefix

# https://leetcode.com/problems/longest-common-prefix/description/

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"



# This is an easy problem , it can be more pytonic using "for items in zip(*strs)"


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for items in zip(*strs):
            if len(set(items))>1:
                return res 
            res+=items[0]
        return res
