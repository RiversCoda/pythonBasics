# https://leetcode.cn/problems/sort-even-and-odd-indices-independently/

class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = sorted(nums[::2])
        odd = sorted(nums[1::2])[::-1]
        nums[::2] = even
        nums[1::2] = odd
        return nums
