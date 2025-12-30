"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
"""

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(i, j):
            s = set()
            for x in range(3):
                for y in range(3):
                    s.add(grid[i + x][j + y])
            if s != set(range(1, 10)):
                return False
            if grid[i][j] + grid[i][j + 1] + grid[i][j + 2] != 15:
                return False
            if grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] != 15:
                return False
            if grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2] != 15:
                return False
            if grid[i][j] + grid[i + 1][j] + grid[i + 2][j] != 15:
                return False
            if grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] != 15:
                return False
            if grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] != 15:
                return False
            if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != 15:
                return False
            if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != 15:
                return False
            return True

        count = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic(i, j):
                    count += 1
        return count