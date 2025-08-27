from collections import deque

"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""


class SolutionTrivial:
    """
    Compute the squares, then sort the values
    O(n log n) because of the sorting algorithm
    """

    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums


class Solution2P:
    """
    Use two pointers on the right and left side.
    Add to the result whatever value has the largest square, and move the pointer accordingly.
    l and r might orverlap. It's finished when l > r
    """

    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        res = []

        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                res.append(nums[l] ** 2)
                l += 1
            else:
                res.append(nums[r] ** 2)
                r -= 1

        res.reverse()
        return res


class Solution2P2:
    """ """

    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        res = []

        lv, rv = nums[l] ** 2, nums[r] ** 2

        while l <= r:
            if lv > rv:
                res.append(lv)
                l += 1
                lv = nums[l] ** 2
            else:
                res.append(rv)
                r -= 1
                rv = nums[r] ** 2

        res.reverse()
        return res


class Solution2P3:
    """
    Same as Solution2P, but using a queue to append on the left,
    Then convert the queue to a list, instead of reversing the list
    """

    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        res = deque()

        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                res.appendleft(nums[l] ** 2)
                l += 1
            else:
                res.appendleft(nums[r] ** 2)
                r -= 1

        return list(res)


nums = [-4, -1, 0, 3, 10]  # -> [0,1,9,16,100]
nums = [-7, -3, 2, 3, 11]  # -> [4,9,9,49,121]

solution = Solution2P3()
res = solution.sortedSquares(nums)
print(res)
