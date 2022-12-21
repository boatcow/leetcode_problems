# 1053. Previous Permutation With One Swap
# https://leetcode.com/problems/previous-permutation-with-one-swap/description/
'''
Given an array of positive integers arr (not necessarily distinct), return the 
lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap. 


If it cannot be done, then return the same array.

Note that a swap exchanges the positions of two numbers arr[i] and arr[j]


Eg: 
Input : [3, 2, 1]
Output : [3, 1, 2]
Explanation: 312 is closest element to 321 , that is smaller  ... with just one swap


Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.

'''

'''
Approach : 
1. Well , if we make 1000's place element smaller, it would impact more than making 100's place element smaller right? 

2. So we try to swap element in lower place, so change is lesser

3. how do we know what place element we need to swap ? 
        in 10's place if there is a smaller element existing in units place => we can swap
        in 1000's place if there is a smaller element in 100's place and 10's place ?
                    => we swap with whichever is greater value but lesser than 1000's place.

So two phases:
    1. find what place element we need to swap=>
            iterate last few elements in array , if it is sorted , then we can't swap
                            => if the sort breaks somewhere, we swap in that place
    2. find max_val to swap which comes after the place and swap

    3. return array
'''



class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i=len(arr)-1

        # find what place the swap would take place
        # 'i' value
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>arr[i+1]:
                break
        
        # swap element closest to 'i' value and closest to 'i' index
        j=i+1
        max_val_closer_to_curr=-1
        max_val_index=-1
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i] and arr[j]>max_val_closer_to_curr:
                max_val_closer_to_curr=arr[j]
                max_val_index=j
        # swap if we could
        if max_val_index!=-1:
            arr[i],arr[max_val_index]=arr[max_val_index],arr[i]

        # return array
        return arr
        