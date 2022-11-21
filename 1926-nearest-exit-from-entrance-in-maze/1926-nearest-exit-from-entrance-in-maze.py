class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r,c = len(maze),len(maze[0])
        i,j = entrance
        queue = deque([(i,j,0)])
        visited = set([(i,j)])
        
        while queue:
            rr,cc,d = queue.popleft()
            if d != 0 and (rr == r - 1 or rr == 0 or cc == c - 1 or cc == 0):
                return d
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr,nc = rr+dr,cc+dc
                if r > nr >= 0 and c > nc >= 0 and maze[nr][nc] != '+' and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,d+1))
        return -1