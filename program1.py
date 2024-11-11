class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
       if not grid:
          return 0

      def dfs(row, col):
         if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W':
            return

         grid[row][col] = 'W'
         dfs(row - 1, col)
         dfs(row + 1, col)
         dfs(row, col - 1)
         dfs(row, col + 1)

      num_islands = 0

      for i in range(len(grid)):
         for j in range(len(grid[0])):
            if grid[i][j] == 'L':
               num_islands += 1

               dfs(i, j)
                    
        return num_islands
