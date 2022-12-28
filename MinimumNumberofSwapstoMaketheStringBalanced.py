# 1963. Minimum Number of Swaps to Make the String Balanced
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

# the idea is a GREEDY ish way,
# since the brackets can always be balanced

# if "]" count till "i" is  > "[" count till "i"
#       => the less balanced it is, ( more swaps to fix ordering )
#       => the other way around , 
#               the same property DOES NOT hold,
#                more "[" till "i" means we will eventually get "]" and dont need swaps to fix

# so we keep a MAX EXCEEDING count of no of "]" > no of "[" till "i"

# since swap does two changes at a time we return the  ( COUNT +1) // 2

class Solution:
    def minSwaps(self, s: str) -> int:
        m,c=0,0
        t=0
        for i in s:
            if i=="]":
                c-=1
            else:
                c+=1
            m=min(m,c)
        return (abs(m)+1)//2
