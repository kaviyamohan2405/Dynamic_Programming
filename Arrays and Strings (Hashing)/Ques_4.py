'''
Question 4: Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the
answer in any order.

Example:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

'''

from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, freq in count.most_common(k)]

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # Output: [1, 2]
