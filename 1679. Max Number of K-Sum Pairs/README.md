## Intuition
The problem asks us to find the maximum number of operations we can perform to sum two numbers in the given nums list to get a result equal to k. To approach this problem, we can consider using a hash map (dictionary in Python) to keep track of the count of each number in the nums list. The idea is to iterate through the list, and for each number num, check if k - num exists in the dictionary and has a count greater than zero. If it does, we can perform an operation and decrement the count of both num and k - num in the dictionary.

## Approach
1. Initialize a variable operation to keep track of the number of operations.
2. Initialize a dictionary num_count to store the count of each number in the nums list.
3. Iterate through the nums list.
4. For each num, check if k - num exists in num_count and has a count greater than zero.
    - If yes, increment the operation count by 1, and decrement the count of both num and k - num in the num_count dictionary.
    - If no, increment the count of num in the num_count dictionary.
5. After iterating through the entire list, return the operation count as the maximum number of operations.
## Complexity
- Time complexity:
The time complexity of this solution is $O(n)$, where n is the number of elements in the nums list. We iterate through the list once.

- Space complexity:
The space complexity is $O(n)$ as well because in the worst case, we may need to store all unique elements of the nums list in the num_count dictionary.