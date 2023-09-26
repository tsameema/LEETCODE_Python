class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      v = ['a', 'e', 'i', 'o', 'u']
      varray = s[:k]
      max_vowels = float('-inf')
      count = sum(1 for j in range(k) if varray[j] in v)
      for i in range(k, len(s)):
        max_vowels = max(count, max_vowels)
        if varray[0] not in v and s[i] in v:
          count += 1
        elif varray[0] in v and s[i] not in v:
          count -= 1
        varray = varray[1:] + s[i]
      return max(max_vowels, count)