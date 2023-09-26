from typing import List
import numpy as np

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
      isplaced = False
      if not 1 <= len(flowerbed) <= np.power(104, 2):
        return isplaced

      if not 0 <= n <= len(flowerbed):
        return isplaced

      bed_len, start = len(flowerbed), 0

      while n and start < bed_len:
        
        if not flowerbed[start] in [0, 1]:
            return False

        if bed_len == 1:
          return True  if flowerbed[start] == 0 else False
            
        if flowerbed[start] == 0:
          if start == 0:
            if flowerbed[start+1] == 0:
              n -= 1
              start += 2
            else:
              start += 2
          
          elif start == bed_len-1:
            if flowerbed[start-1] == 0:
              n -= 1
              start += 2
            else:
              start += 2

          elif 0 < start < bed_len-1:
            if flowerbed[start-1] == 0 and flowerbed[start+1] == 0:
              n -= 1
              start += 2
            else:
              start += 1
        else:
          start+=1

        if start >= bed_len:
          break
      
      return False if n>0 else True