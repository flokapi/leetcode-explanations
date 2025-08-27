class Solution:
    """
    Define the current boundaries, first start with the matrix size
    Then iterate on the matrix boundaries in a circle, until there are not points left
    """

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        x1, x2 = 0, len(matrix[0]) - 1
        y1, y2 = 0, len(matrix) - 1

        res = []

        while True:
            for x in range(x1, x2 + 1):
                res.append(matrix[y1][x])
            y1 += 1
            if y1 > y2:
                break

            for y in range(y1, y2 + 1):
                res.append(matrix[y][x2])
            x2 -= 1
            if x1 > x2:
                break

            for x in range(x2, x1 - 1, -1):
                res.append(matrix[y2][x])
            y2 -= 1
            if y1 > y2:
                break

            for y in range(y2, y1 - 1, -1):
                res.append(matrix[y][x1])
            x1 += 1
            if x1 > x2:
                break

        return res


class SolutionDynamic:
    """
    Update the matrix object while adding the result
    Add conditions to perform the operation only if feasable
    Use while loop condition to know when to exit loop
    """

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []

        while matrix:
            res += matrix.pop(0)

            if matrix and matrix[0]:
                for y in range(len(matrix)):
                    res.append(matrix[y].pop())

            if matrix:
                res += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for y in range(len(matrix) - 1, -1, -1):
                    res.append(matrix[y].pop(0))

        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
solution = SolutionDynamic()
res = solution.spiralOrder(matrix)
print(res)
