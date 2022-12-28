# 1930. Unique Length-3 Palindromic Subsequences
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/


# well, since we have to find all palindromes with size "3" ( 3 is always default )
# it is just finding the 
    # left most occurance of character x and right most occurance of the same character x
    # and len ( set ( string [index of left occurance+1 : index of right occurance] ) ) = 
                         # i.e all unique characters between left and right

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        visited=set()
        tot=0
        for c in s:
            if c in visited:
                continue
            visited.add(c)
            l=s.find(c)
            r=s.rfind(c)
            tot+=len(set(s[l+1:r]))
        return tot