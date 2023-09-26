from typing import List

class Solution:
  def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    list1_2 = [[], []]
    for n1 in set(nums1):
      if n1 not in nums2:
        list1_2[0].append(n1)
    for n2 in set(nums2):
      if n2 not in nums1:
        list1_2[1].append(n2)
    
    return list1_2