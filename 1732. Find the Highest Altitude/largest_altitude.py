from typing import List

class Solution:
  def largestAltitude(self, gain: List[int]) -> int:
    current_altitude = 0
    complete_altitude = []
    for i in range(len(gain)):
      current_altitude += gain[i]
      complete_altitude.append(current_altitude)
    max_altitude = 0
    for altitude in complete_altitude:
      if max_altitude < altitude:
        max_altitude = altitude
    return max_altitude