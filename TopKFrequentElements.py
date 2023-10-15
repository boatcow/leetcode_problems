# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# As the problem states, we need to print top k frequent elements.


# Of course we can store frequency in a dictionary , sort and return , but that's nLog(n)

# is there a better solution?


# Clue : Counting Sort , i.e array where index is frequency and value is the number.