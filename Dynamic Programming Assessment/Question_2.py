'''Question 2

Problem Description:

Given a string `s`, return the longest palindromic substring in `s`.

Input Description:
A string `s`.

Output Description:
The longest palindromic substring in `s`.

Examples:
**Example 1:**
- Input: `s = "babad"`
- Output: `"bab"`
- Explanation: `"aba"` is also a valid answer.
**Example 2:**
- Input: `s = "cbbd"`
- Output: `"bb"`
Constraints:
1 <= s.length <= 1000
s consists of only digits and English letters.'''


# CODING PART

def longestPalindrome(s):
    if len(s) == 0:
        return ""

    start = 0
    max_length = 1

    for i in range(len(s)):
        # Odd length palindromes (center is at i)
        len1 = expandAroundCenter(s, i, i)
        # Even length palindromes (center is between i and i+1)
        len2 = expandAroundCenter(s, i, i + 1)

        max_len = max(len1, len2)
        if max_len > max_length:
            max_length = max_len
            start = i - (max_len - 1) // 2

    return s[start:start + max_length]

def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

# Example usage
s = "cbbd"
print(longestPalindrome(s))  # Output: "bb"

s = "babad"
print(longestPalindrome(s))  # Output: "bab"

