"""

Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    i = 0
    j = 1

    while j in range(1,len(nums)):
        if nums[i] == nums[j]:
            j = j + 1
        else:
            nums[i+1] = nums[j]
            i = i + 1
            j = j + 1
    del nums[i+1:]
    return i+1

