## Intuition
The problem asks us to determine if the number of occurrences of each unique element in the input array is itself unique. In other words, we need to check if no two different elements in the array have the same count. To solve this problem, we can use a dictionary to keep track of the count of each unique element and then check if the set of counts is of the same size as the number of unique elements.

## Approach
1. Initialize an empty dictionary dict_occur to store the count of each unique element and an empty list list_unique to store the unique counts.
2. Iterate through the elements of the input array arr.
    - If the element a is not in the dict_occur keys, add it with a count of 1.
    - If the element a is already in dict_occur keys, increment its count by 1.
3. Iterate through the items in dict_occur to extract the counts and check if they are unique.
    - If a count is not in list_unique, add it to list_unique.
4. Finally, check if the length of dict_occur.values() (which contains all the counts) is equal to the length of list_unique.
    - If they have the same length, return True because it means all counts are unique.
    - Otherwise, return False.
## Complexity
- Time complexity:
The algorithm iterates through the input array once to count occurrences, and then it iterates through the counts in the dictionary once. Therefore, the time complexity is O(n), where n is the number of elements in the input array.

- Space complexity:
The space complexity is O(m), where m is the number of unique elements in the input array. This is because we are using a dictionary to store counts and a list to store unique counts. In the worst case, when all elements are unique, m is equal to n, and the space complexity is O(n).