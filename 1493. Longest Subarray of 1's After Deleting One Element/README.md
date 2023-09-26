## Intuition
The problem asks us to find the length of the longest subarray consisting of only 1s after removing at most one 0 from the array. To solve this problem, we can iterate through the given array while keeping track of the count of consecutive 1s and the positions of 0s encountered. When we encounter a 0, we can consider removing it and combining the consecutive 1s on both sides of the 0 to calculate the length of the resulting subarray. We should keep track of the maximum subarray length encountered during the iteration.

## Approach
1. Initialize variables ones as an empty list to store the counts of consecutive 1s, c as 0 to count consecutive 1s, and max_len as 0 to store the maximum subarray length.
2. Iterate through the nums array using a for loop:
    - If the current element nums[i] is 1, increment the c variable to count consecutive 1s.
    - If the current element nums[i] is 0, append the value of c to the ones list, indicating the count of consecutive 1s encountered before the 0, and reset c to 0.
3. After the loop, if the last element of the nums array is 1 (i.e., nums[i] == 1), append the final value of c to the ones list.
4. Initialize max_len as the first element of the ones list (if it exists). This is the length of the longest subarray starting from the beginning of the array.
5. Iterate through the ones list starting from the second element (index 1) to calculate the maximum subarray length. For each element ones[i], compare it with the sum of the previous element ones[i-1] and the current element ones[i]. Update max_len with the maximum of these two values.
6. Return max_len as the length of the longest subarray consisting of only 1s after removing at most one 0.
## Complexity
- Time complexity:
$O(n)$, where n is the length of the nums array. We perform a single pass through the array to calculate the longest subarray length.

- Space complexity:
$O(n)$, as we use the ones list to store counts of consecutive 1s. In the worst case, all elements in the nums array are 1s, and the ones list would have the same length as nums.