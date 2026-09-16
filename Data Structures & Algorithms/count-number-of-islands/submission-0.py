class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                if grid[i][j] == '0':
                    continue
                visited = self.bfs((i,j), grid, visited)
                islandCount += 1
        return islandCount
    
    def bfs(self, point, grid, visited):
        q = collections.deque([point])
        visited.add(point)
        while q:
            i, j = q.popleft()
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    if grid[ni][nj] =='1' and (ni, nj) not in visited:
                        q.append((ni,nj))
                        visited.add((ni, nj))

        return visited