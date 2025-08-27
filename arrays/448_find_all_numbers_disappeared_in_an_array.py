class Solution1:
    """
    Create the set of the numbers and the expected set
    Return the difference of the sets as a list
    Time: O(n)
    """

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s_nums = set(nums)
        s_exp = set(range(1, len(nums) + 1))
        return list(s_exp - s_nums)


class Solution2:
    """
    Create the set of the given numbers
    Iterate on the expected numbers, add to the result the missing ones
    Slightly better in term of memory, also O(n)
    """

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s_nums = set(nums)

        res = []
        for num in range(1, len(nums) + 1):
            if num not in s_nums:
                res.append(num)
        return res


class Solution3:
    """
    Create the set of the given numbers
    Reuse the input array to produce the response
    Sligthly better in term of memory, also O(n)
    """

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s_nums = set(nums)

        res_count = 0
        for num in range(1, len(nums) + 1):
            if num not in s_nums:
                nums[res_count] = num
                res_count += 1

        return nums[:res_count]


class Solution4:
    """
    Define the set of the expected numbers
    Iterate on the given numbers and remove them from the set if present
    Return the remainer as a list
    """

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s_exp = set(range(1, len(nums) + 1))
        for num in nums:
            if num in s_exp:
                s_exp.remove(num)
        return list(s_exp)


class SolutionDp:
    """
    Use extra memory to save whether a number was found using its index
    Add all the missing numbers to the result
    Time O(n), Space O(n)
    """

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        buf = [False] * len(nums)

        for i in nums:
            buf[i - 1] = True

        res = []
        for i in range(len(buf)):
            if buf[i] is False:
                res.append(i + 1)
        return res


class SolutionDpConstantSpace:
    """
    Officially Time O(n), Space O(1)
    Keep the record of which number exists by reusing the nums array.
    Since all numbers are positive, we can change the sign of the number to mark
    its presence at a given index, which is O(n)
    Index i => number i + 1
    Then, return the corresponding numbers at the index which still have a positive sign
    """

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for n in nums:
            i = abs(n) - 1
            if nums[i] > 0:
                nums[i] *= -1

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res


nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution = SolutionDp()
res = solution.findDisappearedNumbers(nums)
print(res)
