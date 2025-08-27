# 11:15


class Solution:
    """
    Time: O(n)
    """

    def longestMountain(self, arr: list[int]) -> int:
        best = 0
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left, right = i, i
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                    right += 1
                best = max(best, right - left + 1)
        return best


class Solution2:
    """
    Complex, didn't work due to edge cases, but might be more efficient

    Increasing
        → if incr , advance i
        → else, decreasing
    Decreasing
        → if decr, advance i
        → else, increasing
        → length = i - start
        → start = i
    """

    def longestMountain(self, arr: list[int]) -> int:
        best = 0
        start, i = None, 0
        increasing = False

        while i != len(arr) - 1:
            if arr[i] == arr[i + 1]:
                i += 1
                if start is not None:
                    start = i
                increasing = True
                continue

            if increasing:
                if arr[i + 1] <= arr[i]:
                    increasing = False
                else:
                    i += 1
            else:
                if arr[i + 1] >= arr[i]:
                    increasing = True
                    if start is not None:
                        best = max(best, i - start + 1)
                    start = i
                else:
                    i += 1

        if not increasing and start is not None:
            best = max(best, i - start + 1)

        return best


arr = [2, 1, 4, 7, 3, 2, 5]  # -> 5
arr = [2, 2, 2]  # -> 0
arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
# arr = [3, 3, 1]

solution = Solution()
res = solution.longestMountain(arr)
print(res)
