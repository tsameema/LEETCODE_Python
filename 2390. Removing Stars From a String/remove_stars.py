class Solution:
    def removeStars(self, s: str) -> str:
        
      stack = []
      for n in s:
        if n=="*":
          stack.pop()
        else:
          stack.append(n)

        
      return "".join(stack)