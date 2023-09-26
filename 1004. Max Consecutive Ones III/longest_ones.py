from typing import List
class Solution:
  def longestOnes(self, nums: List[int], k: int) -> int:
    left = zero = max_length = 0
    for i in range(len(nums)):
      if nums[i]==0:
        zero += 1
      while zero > k:
        if nums[left] == 0:
          zero -= 1
        left += 1
      max_length = max(max_length, i-left+1)
    return max_length