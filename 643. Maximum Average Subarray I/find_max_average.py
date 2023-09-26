from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
      max_avg_val = float('-inf')
      sum_array = sum(nums[:k])
      for i in range(k, len(nums)):
        max_avg = sum_array/k
        if max_avg_val<max_avg:
          max_avg_val = max_avg 
        sum_array += nums[i] - nums[i-k]
      return max(max_avg_val, sum_array/k)