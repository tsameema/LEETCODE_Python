## Intuition
The problem asks us to find the maximum average of any contiguous subarray of length k. To solve this problem, we can use a sliding window approach to efficiently compute the sum of subarrays of length k and keep track of the maximum average seen so far.

## Approach
Here's our approach to solving the problem:

1. Initialize max_avg_val to negative infinity. This variable will keep track of the maximum average seen so far.

2. Compute the sum of the first k elements of the nums array and store it in sum_array. This represents the sum of the initial subarray of length k.

3. Iterate over the nums array starting from index k to the end of the array. At each step, do the following:
    - Compute the average of the current subarray of length k by dividing sum_array by k.
    - Update max_avg_val with the maximum of its current value and the computed average.
    - Update sum_array by subtracting the element that is no longer part of the current subarray (at index i - k) and adding the current element (at index i).
4. After the loop, return the maximum of max_avg_val and the average of the last subarray (which extends to the end of the array).

## Complexity
- Time complexity:
 The algorithm iterates through the nums array once, performing constant-time operations at each step. Therefore, the time complexity is $O(n)$, where n is the length of the nums array.

- Space complexity:
The algorithm uses a constant amount of additional space to store variables, so the space complexity is $O(1)$.