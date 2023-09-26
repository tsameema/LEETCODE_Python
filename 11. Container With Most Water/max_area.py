from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
      left = 0
      right = len(height)-1
      area = []
      while left < right:
        if height[left] >= height[right]:
          area.append(height[right] * (right-left))
          right-=1
        else:
          area.append(height[left]* (right-left))
          left+=1
      
      return max(area)