class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            p1, p2 = points[i], points[i + 1]
            res += max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

        return res


class Solution2:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        res = 0
        p1 = points.pop()
        while points:
            p2 = points.pop()
            res += max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
            p1 = p2

        return res


points = [[1, 1], [3, 4], [-1, 0]]
solution = Solution()
res = solution.minTimeToVisitAllPoints(points)
print(res)
