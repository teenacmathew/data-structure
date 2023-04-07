"""
 Longest Common Prefix

    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

"""

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""
    for i in range(len(strs[0])):
        for s in strs[1:]:
            if i==len(s) or  s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix
print(["flower","flow","flight"])
print(longestCommonPrefix(["flower","flow","flight"]))
print(["dog","racecar","car"])
print(longestCommonPrefix(["dog","racecar","car"]))
