# 1081. Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


# Given a string s, return the 
# lexicographically smallest subsequence
#  of s that contains all the distinct characters of s exactly once.

# NOTE : this is subsequence , not substring

# so two pointers, sliding window is no go
'''
Approach : 

1. we add each new character in stack , that is lexicographically in a current order

2. if the new character, is NOT lexigraphically greater than previous element in stack:
     => we recursively remove elements in stack till we can add the new element
     => we DO NOT remove the element in stack, if :
                => the element we are removing doesn't occur again in rest of the string
                => we can ignore doing this if the character already exists in stack

3. return stack as joined string
'''


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            character=s[i]
            while stack and character not in stack and ord(character)<ord(stack[-1]) and stack[-1] in s[i+1:]:
                stack.pop(-1)
            if character not in stack:
                stack.append(character)
        return ''.join(stack)        
        
          
