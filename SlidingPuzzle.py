# 773. Sliding Puzzle
# https://leetcode.com/problems/sliding-puzzle/


# The trick is to use B.F.S not DFS..

# we are trying to find the minimum number of moves here, DFS would be expensive and difficult to figure out when to stop recursing.
# BFS is more straightforward

from collections import defaultdict
import copy

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visited=defaultdict(lambda:False)
        # this function can be avoided as well
        def get_zero_position(sb):
            for i in range(2):
                for j in range(3):
                    if sb[i][j]==0:
                        return [i,j]
        def bfs(b):
            queue=[[b,0]]
            visited=set()
            while queue:
                curr=queue.pop(0)
                if str(curr[0]) in visited:
                    continue
                if curr[0] == [[1, 2, 3], [4, 5, 0]]:
                    return curr[1]
                visited.add(str(curr[0]))
                z=get_zero_position(curr[0])
                up=[z[0]-1,z[1]]
                if up[0]>=0:
                    # not much optimizations
                    temp=copy.deepcopy(curr[0])
                    temp[up[0]][up[1]],temp[z[0]][z[1]]=temp[z[0]][z[1]],temp[up[0]][up[1]]
                    queue.append([temp,curr[1]+1])
                down=[z[0]+1,z[1]]
                if down[0]<=1:
                    temp=copy.deepcopy(curr[0])
                    temp[up[0]][up[1]],temp[z[0]][z[1]]=temp[z[0]][z[1]],temp[up[0]][up[1]]
                    queue.append([temp,curr[1]+1])
                left=[z[0],z[1]-1]
                if left[1]>=0:
                    temp=copy.deepcopy(curr[0])
                    temp[left[0]][left[1]],temp[z[0]][z[1]]=temp[z[0]][z[1]],temp[left[0]][left[1]]
                    queue.append([temp,curr[1]+1])
                right=[z[0],z[1]+1]
                if right[1]<=2:
                    temp=copy.deepcopy(curr[0])
                    temp[right[0]][right[1]],temp[z[0]][z[1]]=temp[z[0]][z[1]],temp[right[0]][right[1]]
                    queue.append([temp,curr[1]+1])
            return -1
        return bfs(board)
            
