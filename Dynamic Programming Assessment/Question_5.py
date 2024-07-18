'''
Question 5

Problem Description:
You are climbing a staircase. It takes `n` steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input Description:
An integer `n`.

Output Description:
The number of distinct ways to climb to the top.

Examples:
**Example 1:**
- Input: `n = 2`
- Output: `2`
- Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
**Example 2:**
- Input: `n = 3`
- Output: `3`
- Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
'''

# CODING PART

def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Example usage
n1 = 2
print(climbStairs(n1))  # Output: 2

n2 = 3
print(climbStairs(n2))  # Output: 3
