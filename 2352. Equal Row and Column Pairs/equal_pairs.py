from collections import defaultdict
from typing import List
class Solution:
  def equalPairs(self, grid: List[List[int]]) -> int:
    col, rows = defaultdict(int), defaultdict(int)
    for i in range(len(grid)):
      col[tuple(grid[j][i] for j in range(len(grid)))] += 1 
      rows[tuple(grid[i])] += 1
    c=0
    for key, val in rows.items():
      if key in col:
        c += val*col[key]
    return c
