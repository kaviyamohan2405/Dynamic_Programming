'''
Question 5: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example:

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

'''

from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

# Example usage
s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # Output: True

s = "rat"
t = "car"
print(is_anagram(s, t))  # Output: False
