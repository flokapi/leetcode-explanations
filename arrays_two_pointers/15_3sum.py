class Solution1:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        past = set()
        n = len(nums)

        res = set()
        for i in range(n):
            for j in range(i + 1, n):
                if -nums[i] - nums[j] in past:
                    res.add(tuple([nums[i], nums[j], -nums[i] - nums[j]]))
            past.add(nums[i])

        return [list(comb) for comb in res]


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n - 2):
            if i and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                v = nums[l] + nums[r] + nums[i]
                if v < 0:
                    l += 1
                elif v > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


nums = [-1, 0, 1, 2, -1, -4]  # -> [[-1,-1,2],[-1,0,1]]
# nums = [0, 1, 1]  # -> []
# nums = [0, 0, 0]  # -> [[0,0,0]]
# nums = [0, 0, 0, 0]

solution = Solution()
res = solution.threeSum(nums)
print(res)
