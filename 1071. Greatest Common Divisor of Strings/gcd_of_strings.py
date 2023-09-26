class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
      word1 = str1.upper()
      word2 = str2.upper()

      if not 1 <= len(word1) <= 1000 and not 1 <= len(word1) <=1000:
        return ""

      if str1+str2 != str2+str1:
        return ""

      str1_len = len(str1)
      str2_len = len(str2)

      while str2_len:
        str1_len, str2_len = str2_len, str1_len % str2_len
      
      return str1[:str1_len] 
        