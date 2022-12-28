# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

# the trick is to keep adding the numbers in num2 to a stack, 
# if the new number we are adding is GREATER THAN the top element in the stack, then
# the element greater than  < stack.pop(-1) = current_element >
# do the above check in a loop


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        d={}
        output=[]
        for i in nums2:
            # keep track of next greater element in a dictionary
            while stack and stack[-1]<i:
                x=stack.pop()
                d[x]=i
            stack.append(i)
        for i in nums1:
            output.append(d.get(i,-1))
        return output

