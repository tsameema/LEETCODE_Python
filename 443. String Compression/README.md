## Intuition
The problem requires us to compress a given list of characters in-place. To do this, we need to count consecutive occurrences of each character and replace them with the character followed by its count. If the count is 1, we should not add a count to the character.

## Approach
1. Initialize an empty string s to store the compressed characters.
2. Initialize a variable count to 1 to keep track of consecutive character counts.
3. Iterate through the input list chars from the first character to the second-to-last character.
Compare the current character with the next character (i.e., chars[i] and chars[i+1]).
    - If they are the same, increment the count by 1.
    - If they are different, add the current character to the s string.
    - If count is greater than 1, append the count as a string to s.
    - Reset the count to 1.
4. After the loop, add the last character to the s string.
    - If the count is greater than 1, append the count as a string to s.
5. Update the chars list with the characters from the s string by converting it to a list.
6. Return the length of the modified chars list.
## Complexity
- Time complexity:
The algorithm iterates through the input list once, so the time complexity is O(n), where n is the length of the input list.

- Space complexity:
The extra space used is the s string, which can be at most O(n) in length in the worst case, so the space complexity is O(n).

