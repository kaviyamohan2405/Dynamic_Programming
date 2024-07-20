'''
Question 3: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''

def length_of_longest_substring(s):
    char_index = {}
    longest = start = 0
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        longest = max(longest, i - start + 1)
    return longest

# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3
