class SolutionDFS:
    """
    It's necessary to go through all the grid.
    If a 1 is found, it means there is an island.
        Use this occasion to "remove" all neighboring 1s to avoid
        counting the island twice.
        This will ensure that the next 1 found corresponds to a new island
    The neighbor search algorithm can use DFS of BFS
        DFS: recursively look on all four sides
        BFS: use a queue to mark the next ones
    Time: O(m*n) - even if for each cell it looks on all 4 sides, O(4*m*n) is still O(m*n)
    Space: O(1) - no extra memory used
    """

    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def find(i: int, j: int):
            if i < 0 or i >= n or j < 0 or j >= m or grid[j][i] == "0":
                return
            grid[j][i] = "0"
            find(i + 1, j)
            find(i - 1, j)
            find(i, j + 1)
            find(i, j - 1)

        res = 0
        for j in range(m):
            for i in range(n):
                if grid[j][i] == "1":
                    res += 1
                    find(i, j)

        return res


class SolutionDFS2:
    """
    Slightly different DFS solution.
    Checks whether a point has to be erased before processing it.
    """

    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def find(i: int, j: int):
            grid[j][i] = "0"
            if i < n - 1 and grid[j][i + 1] == "1":
                find(i + 1, j)
            if i > 0 and grid[j][i - 1] == "1":
                find(i - 1, j)
            if j < m - 1 and grid[j + 1][i] == "1":
                find(i, j + 1)
            if j > 0 and grid[j - 1][i] == "1":
                find(i, j - 1)

        res = 0
        for j in range(m):
            for i in range(n):
                if grid[j][i] == "1":
                    res += 1
                    find(i, j)

        return res


class SolutionBFS:
    """
    BFS solution.
    Instead of using a set to record the visited cells, erases the island cells.
    /!\: The cells must be marked immediately after being added to the new_queue
         Otherwise, there will be duplicates.
    Time: O(m*n)
    Space: O(m+n)
    """

    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(i: int, j: int):
            grid[j][i] = "0"
            queue = [(i, j)]

            while queue:
                new_queue = []
                while queue:
                    x, y = queue.pop()
                    for xp, yp in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        xs, ys = x + xp, y + yp
                        if 0 <= xs < n and 0 <= ys < m and grid[y + yp][x + xp] == "1":
                            new_queue.append((xs, ys))
                            grid[ys][xs] = "0"
                queue = new_queue

        res = 0
        for j in range(m):
            for i in range(n):
                if grid[j][i] == "1":
                    res += 1
                    bfs(i, j)

        return res


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
grid = [
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "0",
        "1",
        "1",
    ],
    [
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
    ],
    [
        "1",
        "0",
        "1",
        "1",
        "1",
        "0",
        "0",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "0",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
    ],
    [
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "1",
        "1",
        "1",
        "1",
        "0",
        "0",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
    [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ],
]
solution = SolutionBFS()
res = solution.numIslands(grid)
print(res)
