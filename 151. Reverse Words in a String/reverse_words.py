class Solution:
    def reverseWords(self, s: str) -> str:
      l, i= [], 0
      for n, w in enumerate(s):
        if w==' ':
          l.append(s[i:n])
          i=n+1
        if n==len(s)-1:
          l.append(s[i:n+1])
      words = ' '.join([w for w in l if w!=''][::-1])
      
      return words