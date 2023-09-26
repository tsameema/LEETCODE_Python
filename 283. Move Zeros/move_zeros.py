from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      count, n = 0, []
      for i in range(len(nums)):
        if nums[i] == 0:
          count+=1
        else:
          n.append(nums[i])
      
      for i in range(count):
        n.append(0)
      
      nums[:] = n[:]

      return None
        