class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        total = sum(nums)

        for i, num in enumerate(nums):
            if left == total - left - num:
                return i

            left += num

        return -1