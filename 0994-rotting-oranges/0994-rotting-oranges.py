class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # 0 = empty
        # 1 = fresh orange
        # 2 = rotten orange
        # fresh orange next to rotten orange turns rotten in 1 minute
        # find min # mniutes until all rotten
        # return -1 if impossible

        # 7:32 - 8:00

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0

        # track fresh orange, add rotten orange to queue
        for r in range(rows):
            for c in range(cols):
                # track # fresh
                if grid[r][c] == 1:
                    fresh += 1

                # add rotten oranges to queue
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            for _ in range(len(q)):
                # remove from queue
                r, c = q.popleft()
                
                # check adjacent directions
                for dr, dc in directions:
                    # if fresh, update to rotten + add to queue
                    row, col = r + dr, c + dc
                    if (row in range(rows) 
                        and col in range(cols) 
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            minutes += 1
            print(minutes, grid)

        # confirm all rotten oranges
        return minutes if fresh == 0 else -1

                    
