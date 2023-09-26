class Solution:
    def reverseVowels(self, s: str) -> str:
      vowels_ = "aeiouAEIOU"
      vowels = [w for w in s if w in vowels_]
      i=len(vowels)
      words = ''.join(word if word not in vowels_ else vowels[i := i - 1] for word in s)
      return words