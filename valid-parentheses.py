"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    hash_map = {
        ')' : '(','}' : '{',']' : '[',
    }
    if len(s)%2 != 0:
        return False
    arr = []
    for i in s:
        if(i == ')' or i == ']' or i == '}' ):
            if(len(arr)==0 or hash_map[i] != arr[-1]):
                return False
            arr.pop(-1)
        else:
            arr.append(i)
    if len(arr) == 0:
        return True
    else:
        return False
       

print("()   ----> " + str(isValid("()")))
print( "()[]{}    ----->  " + str(isValid( "()[]{}")))
print("(]   ----->  " + str(isValid("(]")))
