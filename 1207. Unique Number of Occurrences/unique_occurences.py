from typing import List
class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    dict_occur, list_unique = {}, []
    for a in arr:
      dict_occur[a] = 1 if a not in dict_occur else dict_occur[a]+1

    val = dict_occur.values()
    return (len(set(val)) == len(val)) 