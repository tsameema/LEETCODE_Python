from collections import defaultdict
from typing import List
class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
      return False

    list1, list2 = [], []
    dict1, dict2 = defaultdict(int), defaultdict(int)
    for w1 in word1:
      if w1 not in list1: #check letters in word1 is also present in word2
        list1.append(w1)
      dict1[w1] += 1  #count number of times each letter of word1 present

    for w2 in word2:
      if w2 not in list2: #check letters in word2 is also present in word1
        list2.append(w2)
      dict2[w2] += 1 #count number of times each letter of word2 present
      
    if sorted(set(list1)) != sorted(set(list2)):
      return False
    if sorted(dict1.values())!= sorted(dict2.values()):
      return False

    return True