# Binary Search 

## Notes

Binary search is an efficient search algorithm with a time complexity of O(log(n)), making use of the divide and conquer principle.

It works by reducing the search interval by half at each iteration, guaranteeing a fast convergence to the interval of interest.

However, it works only on sorted arrays. Sorting an array would have a time complexity of O(n log(n)).

The main challenges are usually: updating the search interval properly, handling the exit conditions as well as the boundary cases.



## 704. Binary Search

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

 

**Example:**

- Input: `nums = [-1,0,3,5,9,12]`, `target = 9`
- Output: `4`



### Approach 1: Search exact value, or exclude segment until pointers cross

If the middle pointer `M ` matches the value, we return the index `M`.

Else, we move the left or the right pointer to reduce the search interval.

- Since we know that `M` doesn't point to the value we are looking for, we can exclude it from the next interval: `L = M + 1` or `R = M - 1` .



![704_1_1](README.assets/704_1_1_.png)



If the value we are looking for is not present in the array, the `L` and `R` pointers will end up crossing each other. We can use this to detect the absence of the searched value.



![704_1_2](README.assets/704_1_2_.png)



```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
```

Time: O(log(n)) - Space: O(1)



## 278. First bad version

You are a product manager and currently leading a team to develop a  new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous  version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.



**Example:**

- Input: `n = 5`,` bad = 4`
- Output: `4`



### Approach 1: 

If the middle value `V` is `False`, the version is good and all previous versions including `V` can be excluded from the search interval.

If `V` is `True`, the version is bad and we can exclude all versions on the right of `V`, but not `V` itself, because it might actually be the first occurrence of the bad version we are looking for.

Once the interval is reduced to a single value, we know that this value will be the first occurrence, at which point we can return the result.



![278_1](README.assets/278_1_.png)



```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            v = (l + r) // 2
            if isBadVersion(v):
                r = v
            else:
                l = v + 1

        return l
```

Time: O(log(n)) - Space: O(1)
