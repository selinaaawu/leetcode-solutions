class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        # if already colored, return
        match = image[sr][sc]
        if match == color:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            # if outside matrix or not correct #, return
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != match:
                return
            
            # update color
            image[r][c] = color

            # visit adjacent neighbors
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)
        return image
