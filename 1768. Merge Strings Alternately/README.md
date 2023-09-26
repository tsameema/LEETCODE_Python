## Overview
This code defines a class Solution with the mergeAlternately method to solve the problem as described in the approach section. It also
includes a check for the length of input words and returns an error message if they are not within the specified range. 
Finally, it demonstrates the usage of the mergeAlternately method with sample input and prints the result.


## Intuition
The problem requires merging two strings alternately, meaning we need to combine the characters from both strings one by one, starting with the first character of the first string, then the first character of the second string, and so on. If one of the strings is longer than the other, we should append the remaining characters from that longer string to the result.

## Approach
To solve this problem, we can follow these steps:

Check if the lengths of both input strings, word1 and word2, are within the specified range (1 <= len(word1), len(word2) <= 100). If not, return an error message.

Find the minimum length between the two input strings, which will determine how many characters we can alternate between the two strings without exceeding their lengths.

Initialize an empty string result to store the merged alternately string.

Loop through the characters at the same index in both word1 and word2 up to the minimum length found in step 2. Append these characters alternately to the result string.

Append the remaining characters from both word1 and word2 (if any) to the result string.

Return the result string as the merged alternately string.

## Complexity
### Time complexity: 
***O(min(len(word1), len(word2)))*** - We loop through both input strings up to their minimum length.

### Space complexity: 
***O(len(word1) + len(word2))*** - We create a new string to store the merged alternately string, which can be at most the sum of the lengths of both input strings.
