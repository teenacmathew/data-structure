"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.


Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    char_dict = {}
    max_count = 0
    count = 0
    i = 0
    while i < len(s):
        if s[i] in char_dict:
            i = char_dict[s[i]] + 1
            max_count = max(max_count, count)
            count = 0
            char_dict = {}
        else:
            count = count + 1
            char_dict[s[i]] = i
            i = i + 1

    return max(max_count, count)


print("abcabcbb     ------>  " + str(lengthOfLongestSubstring("abcabcbb")))
