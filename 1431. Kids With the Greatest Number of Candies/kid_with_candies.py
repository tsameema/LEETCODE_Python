from typing import List 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      max_candies = max(candies)
      bool_list = [candy + extraCandies >= max_candies for candy in candies]
      return bool_list