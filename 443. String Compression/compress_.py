from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
      if len(chars) == 1:
        return 1
      else:
        count, s = 1, ''
        for i in range(0, len(chars)-1):
          if chars[i] == chars[i+1]:
            count +=1
          else:
            s+=chars[i]
            if count > 1:
              s+=str(count)
              count=1

        s += chars[-1]
        if count > 1:
            s += str(count)

      chars[:] = list(s)
      return len(chars)