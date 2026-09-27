class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # 6:30 - 6:50
        rows, cols = len(grid), len(grid[0])
        islands = 0

        # explores entire island
        def dfs(r, c):
            # skip if water or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            
            # mark as visited
            grid[r][c] = "0"

            # explore adjacent 
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # check all cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands
        