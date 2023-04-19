"""

Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

"""



def reverse( x):
    """
    :type x: int
    :rtype: int
    """

    num = abs(x)
    rev = 0
    negate = False

    if x < 0:
        negate = True
    while num > 0:
        rev  = (rev*10) + int(num%10)
        num = int(num / 10)

    if negate:
        rev = rev * -1
    if rev <= -2**31  or rev >= 2**31 -1:
        return 0
    else:
        return rev



print(" 123  ----->  " + str(reverse(123)))
print(" -123  ----->  " + str(reverse(-123)))
print("  120 ----->  " + str(reverse(120)))




