# 2017. Grid Game
# https://leetcode.com/problems/grid-game/

# The question is given a matrix with 2 rows and C columns
# each index in the matrix has a SCORE

# There are two players , both of their objectives is to go from 0,0 to 2,C-1
                                               # i.e top left to bottom right

# player 1 plays 1st:
    # whatever tile he visits, becomes 0
    # his objective is to make sure Player 2 score is MINIMIZED

# player 2 plays 2nd:
    # his objective is to maximize his score,
    # NOTE: the tiles visited by player 1 is 0 now.

# movements: LEFT or DOWN

# NOTE: Player 1's objective isn't to make sure his score is high,
#                   but to make sure Player 2 can't get a good score/

'''
APPROACH:

1. Well, since the number of rows is always 2,  each player can go down , just once

2. The only decision we care about  is , when each player decides to go down.

3. for a given matrix
[2,5,4]
[1,5,1]

When player 1 plays, his path can be like : 

[0,5,4]  OR  [0,0,4]  OR [0,0,0]
[0,0,0]      [1,0,0]     [1,5,0]

Now whatever path player two takes,
=> (his Row1 score will always be 0) OR (his Row2 score will always be 0)
    => this is an interesting property we will be using to solve this problem.


4. We will be creating a prefixSum of row1 from 0 to C
    and We will be creating a prefixSum of row2 from C to 0
    
    Why are we doing this?
            for any particular column, (prefixMatrix[i][0] + prefixMatrix[i][1]) 
            will give total path sum of Player 1
    
    # for player two this will be MAX of (ROW1 PrefixSum[-1] - PrefixSum[i],  ROW2 PrefixSum[0] - PrefixSum[i]_
    # we minimize the above score to find the result

'''

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        nc=len(grid[0])
        row1Sum=[grid[0][i] for i in range(nc)]
        row2Sum=[grid[1][i] for i in range(nc)]
        res=float('inf')
        for i in range(1,nc):
            row1Sum[i]+=row1Sum[i-1]
            row2Sum[nc-i-1]+=row2Sum[nc-i]
        for i in range(nc):
            m=row1Sum[i]+row2Sum[i]  # player 1 score when he goes down at index i
            m2=max(row1Sum[-1]-row1Sum[i],row2Sum[0]-row2Sum[i])  # player 2 score if player 1 goes down at index i
            res=min(res,m2)  # player 1 trying to minimize player 2's score
        return res
            