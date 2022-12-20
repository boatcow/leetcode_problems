# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/


# The trick is ,
# for every index, if you consider the value to be the height of the rectangle,
# we need to find the left most index where the rectangle ends, 
# and the right most index where the rectangle ends
# so area = height * (right-left+1)
# if we brute force this , it will be 0(n) * number of indices = 0(n^2)


# to optimze this we need to use a dictionary or stack

# if we use a dictionary: 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        # keep a track of next smallest value in left , and next smallest value in right
        left,right={},{}
        
        # create a fake height as default, so for the first pillar lowest left element is 0 
        # right element lowest right element is len-1 
        heights=[-1]+heights+[-1]
        left[1]=0
        right[len(heights)-2]=len(heights)-1
        
        #populate left dictionary
        for i in range(2,len(heights)-1):
            lowest_left_i=int(i)-1
            #check if the element in [i-1] is lesser than i, if yes, awesome
            #if no, i.e it is greater, find the next smallest element of (i-1) recursively
            while(heights[lowest_left_i]>=heights[i]):
                lowest_left_i=left[lowest_left_i]
            left[i]=lowest_left_i
        # same as above
        for i in range(len(heights)-2,0,-1):
            lowest_right_i=int(i)+1
            while(heights[lowest_right_i]>=heights[i]):
                lowest_right_i=right[lowest_right_i]
            right[i]=lowest_right_i
        m=0
        # find max and return
        for k in left.keys():
            m=max(heights[k]*(right[k]-left[k]-1),m)
        return m



# dictionary sucks? use a stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)+2
        heights.append(-1)
        heights=[-1]+heights
        left=[0 for _ in range(n)]
        right=[0 for _ in range(n)]
        left_limit_stack=[0]
        right_limit_stack=[len(heights)-1]

        # same stuff, except we pop the stack till we find the smaller element

        for i in range(1,len(heights)-1):
            while(heights[left_limit_stack[-1]]>=heights[i]):
                left_limit_stack.pop(-1)
            left[i]=(left_limit_stack[-1])    
            left_limit_stack.append(i)

            while(heights[right_limit_stack[-1]]>=heights[n-i-1]):
                right_limit_stack.pop(-1)
            right[n-i-1]=(right_limit_stack[-1])
            right_limit_stack.append(n-i-1)
            
        width=[]
        m=0
        for i in range(1,len(left)-1):
            m=max(m,heights[i]*(right[i]-left[i]-1))
        return m


# even better way to do this

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack=[-1]
        m=0
        for i in range(len(heights)):
            while(heights[i]<heights[stack[-1]]):
                # What's happening?
                # whenever we are popping, 
                # use the pop element and find its area
                #
                # how do we know the width you ask?
                # well, the index whose next smallest element we are finding is the MAX the right can go
                # and the stack element stored before it tracks the MAX left it can go
                h=heights[stack.pop(-1)]
                w=i-stack[-1]-1
                m=max(m,h*w)
            stack.append(i)
        return(m)