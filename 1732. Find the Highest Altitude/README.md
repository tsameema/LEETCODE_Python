## Intuition
The problem asks us to find the highest altitude reached during a journey based on a given list of gain values at different points in time. To solve this problem, we can start with an initial altitude of 0 and then iteratively update the current altitude based on the gain values. Our intuition is to keep track of the highest altitude encountered during the journey.

## Approach
Here's a step-by-step explanation of our approach:

1. Initialize two variables: current_altitude to 0 (starting altitude) and max_altitude to 0 (maximum altitude encountered during the journey).

2. Iterate through the gain list, which represents the altitude gain at each step of the journey.

3. At each step, update the current_altitude by adding the gain value at that step to it. This simulates the journey's altitude changes as we move forward.

4. Check if the current_altitude is greater than the max_altitude. If it is, update max_altitude with the value of current_altitude.

5. Continue this process until you have iterated through all the elements in the gain list.

6. Once the loop is finished, max_altitude will hold the highest altitude encountered during the journey.

7. Return max_altitude as the final result.

## Complexity
- Time complexity:
The time complexity of this solution is $O(n)$, where n is the length of the gain list. We iterate through the list once to compute the maximum altitude.

- Space complexity:
The space complexity is $O(n)$ as well because we create a complete_altitude list to store the altitude at each step of the journey, and its length is equal to the length of the gain list.