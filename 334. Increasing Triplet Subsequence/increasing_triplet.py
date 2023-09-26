class Solution:
    def increasingTriplet(self, nums):
      left = middle = float('inf')
      if len(nums) >= 3:
        for right in nums:
          if right<left:
            left=right
          elif left<right<middle:
            middle=right
          elif right>middle:
            return True
      return False
        