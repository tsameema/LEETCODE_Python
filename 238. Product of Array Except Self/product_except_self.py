from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      right = [1]*len(nums)
      right_product = 1
      left = [1]*len(nums)
      left_product = 1

      for n in range(len(nums)):
        left[n] *= left_product
        left_product *= nums[n]

      for n in range(len(nums)-1, -1, -1):
        right[n] *= right_product
        right_product *= nums[n]

      prod_list = [left[n] * right[n] for n in range(len(nums))]
    
      return prod_list