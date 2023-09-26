
## Overview
This code reverses the order of vowels in the input string while keeping the positions of non-vowel characters unchanged. It has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string 's'.


## Intuition
We want to reverse the order of vowels in the given string while keeping the positions of non-vowel characters unchanged.


## Approach
1. Create a string 'vowels_' containing all lowercase and uppercase vowels.
2. Create a list 'vowels' that contains all the vowels from the input string 's'
3. Initialize an index 'i' to the length of 'vowels'.
4. Iterate through each character 'word' in 's':
   - If 'word' is not a vowel, keep it as it is.
   - If 'word' is a vowel, replace it with the vowel at index 'i-1' and decrement 'i'.
5. Join the modified characters to form the final reversed-vowel string and return it.


## Complexity
### - Time complexity:
$O(n)$, where n is the length of the input string 's'.

### - Space complexity:
$O(n)$, as we store the vowels in a list.
