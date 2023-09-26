from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
      operation =  0
      num_count = defaultdict(int)
      for num in nums:
        print(num_count[k-num])
        if num_count[k-num]>0:
          operation += 1
          num_count[k-num] -= 1
        else:
          num_count[num] += 1
      return operation