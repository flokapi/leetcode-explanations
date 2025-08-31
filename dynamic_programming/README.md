# Dynamic programming

Dynamic programming is usually used for problems which include an explosion of possibilities to consider. DP algorithms usually trade complexity for memory.

The main idea is:

- to cut the problem into smaller problems down to the trivial case.
- then to solve the problem bottom up, deducing the properties of the larger system from the smaller one.

Dynamic programming problems can often also be solved using Depth First Search algorithms. This is usually done first by defining a tree of states used for the problem resolution. The explosion of possibilities can be avoided with a mapping which enables reusing the already computed values for each state.



## 322. Coin change

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.



**Example:**

- Input: `coins = [1,2,5]`, `amount = 11`
- Output: `3`



### Approach 1: Report the coin count by cell & coin

Initialize the DP buffer representing the coin count for each value.

- `-1` means not reached yet.
- the starting point is the index `0`  has the value `0`, which means that we can get zero with zero coins.  

While iterating on all values from zero till the target amount:

- If the value can be reached by a given amount of coins, update the cells which correspond to one more coin. But only do so if there is no value yet, or we can write a lower value.

By doing so, we effectively reduce the problem size by one at each step, until we reach the amount cell, which contains the result.

If the amount couldn't be reached, the value of it's cell will remain to `-1`.



![322_1](README.assets/322_1_.png)



```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coin_count = [-1] * (amount + 1)
        coin_count[0] = 0

        for val in range(amount + 1):
            if coin_count[val] == -1:
                continue
            count = coin_count[val]
            for coin in coins:
                if val + coin > amount:
                    continue
                if coin_count[val + coin] == -1 or count + 1 < coin_count[val + coin]:
                    coin_count[val + coin] = count + 1

        return coin_count[-1]
```

Time: O(coin_count * amount) - Space: O(amount)



### Approach 2: Report the coin count by cell & coin, but backwards

Similar to the previous approach. The differences being that:

- We initialize the DP buffer with `float("inf")`, which will simplify the coin count update.
- We update backwards, checking if the current cell needs to be updated depending on already updated cells.

```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for val in range(1, amount + 1):
            for coin in coins:
                if val - coin < 0:
                    continue
                dp[val] = min(dp[val], 1 + dp[val - coin])

        return dp[amount] if dp[amount] != float("inf") else -1
```

Time: O(coin_count * amount) - Space: O(amount)



### Approach 3: Report the coin count by coin & cell

This approach looks similar to the previous one, but we first add one coin on the whole buffer, then the next, ...



![322_3](README.assets/322_3_.png)



```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1
```

Time: O(coin_count * amount) - Space: O(amount)



### Approach 4: Breath First Search using a boolean array

Using this approach, the buffer only contains a boolean, indicating whether we are able to reach a given value, but no coin count information.

We can update the buffer together with a `coin_count` variable, effectively using BFS to search for newly reached values.

If we reach the amount cell, we can return the number of iterations. If the amount can't be reached, the search will stall and there will be no buffer update, at which point we can end the search.

/!\ The issue with this approach is its time complexity, since we need potentially `amount` iterations, each iteration potentially requires checking all coins for all cells.



![322_4](README.assets/322_4_.png)



```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [True] + [False] * amount
        count = 0
        updated = True

        while updated:
            if dp[amount]:
                return count

            updated = False
            count += 1

            for val in range(amount, -1, -1):
                if dp[val]:
                    for coin in coins:
                        if val + coin > amount or dp[val + coin]:
                            continue
                        dp[val + coin] = True
                        updated = True

        return -1
```

Time: O(coin_count * amount²) - Space: O(amount)



### Approach 4: Breath First Search using a bitmask

It works like the previous approach, but we can use a single number to represent all reached values using the bitmask technique.

By doing so, we can manipulate multiple bits in a single operation, making this solution very fast.

If there is a way to reach the amount, it has to be done in `amount + 1` iterations. Otherwise we return `-1`.

```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        curr = 1 << amount
        for i in range(amount + 1):
            if curr & 1 == 1:
                return i
            prev = curr
            curr = 1 << amount
            for coin in coins:
                curr |= prev >> coin
        return -1
```

Time: O(coin_count * amount)
