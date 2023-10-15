'''
problem : https://leetcode.com/problems/graph-valid-tree/ 
https://www.lintcode.com/problem/178

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 

write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Example 2:
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.


Soln : 

DFS with two objectives : check if there is a loop (use visited and prev node to find this) , total visited node == n

'''

from typing import (
    List,
)
from collections import defaultdict
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        graph = defaultdict(set)
        visited=set()
        for to,fr in edges:
            graph[to].add(fr)
            graph[fr].add(to)
        def dfs(node,prev):
            nonlocal graph
            res=True
            if node in visited:
                return False
            visited.add(node)
            for next_node in graph[node]:
                if next_node==prev:
                    continue
                res=res and dfs(next_node,node)
            return res
        return dfs(0,None) and len(visited)==n
            
