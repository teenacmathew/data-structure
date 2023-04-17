"""

Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""



def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int

    """
    print(nums)
    print(val)
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j = j + 1
        i = i + 1
    del nums[j:]
    print(nums)



removeElement([3,2,2,3], 3)

