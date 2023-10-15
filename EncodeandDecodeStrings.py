# 659 · Encode and Decode Strings
# https://www.lintcode.com/problem/659/

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Given a list of strings , encode and send encoded string



# Soln : 

# I would combine all strings in list, and add a start with # + len(word) + # ,
# use #<length of word># to decode a length of word tells the range
