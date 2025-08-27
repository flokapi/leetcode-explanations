class SolutionSortedList:
    """
    Sorts the numbers while keeping the original index information
    Time: O(n log(n)) ; Space: O(n)
    Use two pointers to find the matching numbers, return the original indexes
    Time: O(n) ; Space: O(1)
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        buf = [(i, val) for i, val in enumerate(nums)]
        buf.sort(key=lambda x: x[1])
        left, right = 0, len(nums) - 1
        while True:
            val = buf[left][1] + buf[right][1]
            if val == target:
                return [buf[left][0], buf[right][0]]
            elif val < target:
                left += 1
            else:
                right -= 1


class SolutionDict:
    """
    Time: O(n), Space: O(n)
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        d_nums = {num: n - i - 1 for i, num in enumerate(reversed(nums))}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in d_nums and i != d_nums[num2]:
                return [i, d_nums[num2]]


class SolutionDict2:
    """
    Time: O(n), Space: O(n)
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            if target - num in map:
                return [map[target - num], i]
            map[num] = i


class SolutionBruteforce:
    """
    Try all combinations of numbers, return indexes if match
    Time: O(n^2), Space: O(1)
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums, target = [2, 7, 11, 15], 9
nums, target = [3, 2, 4], 6
nums, target = [3, 3], 6

solution = SolutionDict2()
res = solution.twoSum(nums, target)
print(res)
