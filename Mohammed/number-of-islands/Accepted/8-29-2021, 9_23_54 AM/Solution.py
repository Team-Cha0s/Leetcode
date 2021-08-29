// https://leetcode.com/problems/number-of-islands

class Solution(object):
    def numIslands(self, grid):
        counter = 0
        rows, cols = len(grid), len(grid[0])
        if not grid: 
            return 0
        
        def DFS(row, col):
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == '1':
                grid[row][col] = '0'
                DFS(row+1, col)
                DFS(row-1, col)
                DFS(row, col+1)
                DFS(row, col-1)
        
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    DFS(row, col)
                    counter += 1
        return counter
        