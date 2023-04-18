"""
Palindrome Number

Given an integer x, return true if x is a palindrome , and false otherwise.
"""

import math
def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    t = x
    r = 0
    while t >0:
        r = 10*r + int(t%10)
        t = int(t/10)
    if r == x:
        return True
    else:
        return False


