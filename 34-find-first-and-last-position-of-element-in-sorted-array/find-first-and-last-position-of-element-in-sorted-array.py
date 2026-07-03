

class Solution:
    def searchRange(self, nums, target):
      left=bisect_left(nums,target)
      right=bisect_right(nums,target)-1
      if left<=right and left < len(nums) and nums[left]==target:
        return [left,right]
      return[-1,-1]  