from typing import List
class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    if all(nums)==1:
      return len(nums)-1
    ones, c = [], 0
    for i in range(len(nums)):
      if nums[i]==1:
        c+=1
      elif nums[i] == 0:
          ones.append(c)
          c=0
    if nums[i]==1:
      ones.append(c)
    max_len = ones[0]
    for i in range(1, len(ones)):
      max_len = max(max_len, ones[i-1]+ones[i])

    return max_len