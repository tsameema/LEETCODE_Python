## Intuition
The problem asks for the index at which the sum of elements to the left of that index is equal to the sum of elements to the right of that index. To solve this problem, we can iterate through the array and for each index, check if the sum of elements to its left is equal to the sum of elements to its right.

## Approach
We can use a simple iterative approach to traverse the array and at each index, calculate the sum of elements to the left and to the right of that index. If the sums are equal, we have found the pivot index, and we return it. If we don't find a pivot index after iterating through the entire array, we return -1.

## Complexity
- Time complexity:
We iterate through the array once, and for each index, we calculate the sum of elements to the left and to the right in constant time.

- Space complexity:
We only use a constant amount of extra space for variables.