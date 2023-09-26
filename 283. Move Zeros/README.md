## Intuition
The problem asks us to move all the zeros in a given list to the end while maintaining the relative order of the non-zero elements. One way to approach this problem is by iterating through the list and keeping track of the count of zeros encountered. Then, we can create a new list to store the non-zero elements in their original order and append the necessary number of zeros to the end of this list.

## Approach
1. Initialize two variables: count to keep track of the number of zeros encountered and n to store the non-zero elements in their original order.

2. Iterate through the input list nums using a for loop.

    - If the current element nums[i] is equal to 0, increment the count variable by 1.

    - Otherwise, append the non-zero element nums[i] to the list n.

3. After iterating through the entire nums list, we know the count of zeros (count) and have stored the non-zero elements in their original order in the list n.

4. Create a for loop to append the necessary number of zeros (equal to count) to the end of the list n.

5. Now, the list n contains all the non-zero elements followed by the zeros in the desired order.

6. Update the nums list to be a copy of the list n. We can achieve this by using slicing (nums[:] = n[:]).

7. Return None as the problem statement doesn't require returning a value.

## Complexity
- Time complexity:
The algorithm iterates through the nums list once, so the time complexity is $$O(n)$$, where n is the length of the input list.

- Space complexity:
The space complexity is $$O(n)$$ as we create a new list n to store the non-zero elements.
