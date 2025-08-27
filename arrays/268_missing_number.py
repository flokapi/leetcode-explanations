class Solution1:
    """
    Time: O(n log(n))
    Because of the sorting algorithm
    """

    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i
        return n


class Solution:
    """
    Time: O(n)
    Because only using sums, proportionally to the length of the array
    """

    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


nums = [3, 0, 1]
nums = [0, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

solution = Solution1()
res = solution.missingNumber(nums)
print(res)
