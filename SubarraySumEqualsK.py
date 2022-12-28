# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# find all possible subarrays that sums to K

# well, generating all subarrays is time consuming ( N^2 )

# instead we create a prefixSum array and ( prefixSumArray[j] - prefixSumArray[i] = Sum between i and j index ) 
# eg: if         array = [1,2,3]
#       prefixSumArray = [1,3,6]

# we iterate from i to n:
#     if prefixSum[i] - K exists in any index before i, we return all posibilities

#  How do we find "any index before i" part?
#  Ans: we create a hashmap that stores (KEY:PrefixSum, VALUE:numberOfOccurances) in the LOOP 
#                                                      (i.e tracking occurances until point i)

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # keey track of NUMBER of prefixSum occurances that equate to the Sum
        prefixSumCounter=defaultdict(int)

        #Keeps track of Cumilative sum from 0 to i
        prefixSumArray=[]

        # prefix sum until index 0 is 0 , no of prefixSums equating to 0 so far is just 1 ..so far
        prefixSumCounter[0]=1 
        
        # initialize prefixSum=0
        prefixSum=0
        
        # result sum
        s=0

        # keep track of prefixSum till index i
        for num in nums:
            prefixSum+=num
            prefixSumArray.append(prefixSum)

        # on a loop, keep adding prefix sums to a dictionary (historical tracking)
        # if newSum-oldSum = k , then the subArray equates to k
        for i in prefixSumArray:
            if i-k in prefixSumCounter:
                s+=prefixSumCounter[i-k]
            if i not in prefixSumCounter:
                prefixSumCounter[i]=0
            # tracking occurances till point i-1
            prefixSumCounter[i]+=1
        
        # return sum
        return s