'''
Question 4

Problem Description:
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

Input Description:
An integer array `nums`.

Output Description:
The sum of the subarray with the largest sum.

Examples:
**Example 1:**
- Input: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- Output: `6`
- Explanation: The subarray `[4, -1, 2, 1]` has the largest sum `6`.
**Example 2:**
- Input: `nums = [1]`
- Output: `1`
- Explanation: The subarray `[1]` has the largest sum `1`.
**Example 3:**
- Input: `nums = [5, 4, -1, 7, 8]`
- Output: `23`
- Explanation: The subarray `[5, 4, -1, 7, 8]` has the largest sum `23`.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4'''


# CODING PART

def maxSubArray(nums):
    if not nums:
        return 0

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums1))  # Output: 6

nums2 = [1]
print(maxSubArray(nums2))  # Output: 1

nums3 = [5, 4, -1, 7, 8]
print(maxSubArray(nums3))  # Output: 23
