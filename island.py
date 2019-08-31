"""
Time: O(mn)
Space: O(1)
Leet: Accept
Problems: None
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0

        def sink(grid, row, col):
            #simple dfs traversal to sink the whole island
            if grid[row][col] == '1':
                grid[row][col] = '0'

                if row>0:
                    sink(grid,row-1,col)
                if col>0:
                    sink(grid,row,col-1)
                if row<len(grid)-1:
                    sink(grid,row+1,col)
                if col<len(grid[0])-1:
                    sink(grid,row, col+1)

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    islands += 1
                    sink(grid, row, column)
        return islands
