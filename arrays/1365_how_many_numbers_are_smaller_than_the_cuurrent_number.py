class Solution:
    """
    Sort the numbers: T O(n log n)
    Build the number to lower count dict
    Build and return the lower count by index list
    Time: O(n log n)
    Space: O(n)
    """

    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        s_nums = sorted(nums)

        d_val = {}
        for i, num in enumerate(s_nums):
            if num not in d_val:
                d_val[num] = i

            return [d_val[num] for num in nums]


class SolutionDp:
    """
    Since the number is small, we can DP and memory to count the occurences without sorting
    We save the occurence at index + 1 because it matters for the higher values
    Then we build the occurence list by looking up the value we need
    Time: O(n)
    Space: O(n)
    """

    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        dp = [0] * 102
        for num in nums:
            dp[num + 1] += 1

        for val in range(1, 102):
            dp[val] += dp[val - 1]

        return [dp[val] for val in nums]


nums = [8, 1, 2, 2, 3]
solution = SolutionDp()
res = solution.smallerNumbersThanCurrent(nums)
print(res)
