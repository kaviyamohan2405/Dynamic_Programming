'''
Question 1

Problem Description
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.You may assume that 
you have an infinite number of each kind of coin.

Input Description:
An integer array `coins` representing coins of different denominations.An integer `amount` representing 
a total amount of money.

Output Description:
The fewest number of coins needed to make up the amount. If the amount cannot be made up, return -1.

Examples:
Example 1:
- Input: `coins = [1, 2, 5]`, `amount = 11`
- Output: `3`
- Explanation: `11 = 5 + 5 + 1`
**Example 2:
- Input: `coins = [2]`, `amount = 3`
- Output: `-1`
**Example 3:**
- Input: `coins = [1]`, `amount = 0`
- Output: `0`
Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4'''

# Coding Part

def coinChange(coins, amount):
    # Create dp array with amount + 1 size and initialize with infinity
    dp = [float('inf')] * (amount + 1)
    
    # Base case: 0 coins needed to make amount 0
    dp[0] = 0
    
    # Iterate over each coin
    for coin in coins:
        # Update dp for all amounts from coin to amount
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # If dp[amount] is still infinity, return -1 (not possible)
    # Otherwise, return dp[amount]
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # Output: 3

coins = [2]
amount = 3
print(coinChange(coins, amount))  # Output: -1

coins = [1]
amount = 0
print(coinChange(coins, amount))  # Output: 0