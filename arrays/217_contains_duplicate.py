class Solution1:
    """
    Sets allow to check the presence of an element with O(1) because use hash table
    This makes a solution in O(n)
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        vals = set()
        for num in nums:
            if num in vals:
                return True
            else:
                vals.add(num)
        return False


class Solution:
    """
    The sorting function is O(n log(n))
    Then check whether two consecutive values are the same
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


class Solution2:
    """
    Shortcut by creating a set with all numbers
    Likely also uses O(n)
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


nums = [1, 2, 3, 1]
# nums = [1, 2, 3, 4]
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

solution = Solution()
res = solution.containsDuplicate(nums)
print(res)
