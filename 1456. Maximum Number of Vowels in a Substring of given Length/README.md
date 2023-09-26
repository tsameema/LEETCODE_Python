# Intuition
The problem requires finding the maximum number of vowels in a substring of length k within the given string s. To solve this problem efficiently, we can use a sliding window approach.

# Approach
1. Initialize a list v containing the vowels 'a', 'e', 'i', 'o', and 'u'.
2. Create a variable varray to store the substring of s of length k starting from the beginning of the string.
3. Initialize max_vowels as negative infinity. This variable will keep track of the maximum number of vowels seen so far.
4. Initialize a variable count to keep track of the number of vowels in the initial varray substring. You can use a generator expression and the sum function to count the vowels in varray.
Iterate through the string s starting from index k. For each character at index i:
5. Update max_vowels by taking the maximum of count and max_vowels.
    - Check if the first character in varray (i.e., varray[0]) is not a vowel, but the current character s[i] is a vowel. If so, increment count by 1.
    - Check if the first character in varray is a vowel, but the current character s[i] is not a vowel. If so, decrement count by 1.
    - Update varray by removing the first character (varray[0]) and appending the current character s[i] to it. This effectively moves the sliding window one position to the right.
6. After the loop, return the maximum of max_vowels and count. This accounts for the case where the last k characters in s have the maximum number of vowels.
# Complexity
- Time complexity:
The algorithm has a time complexity of $O(n)$, where n is the length of the input string s. This is because we iterate through the string once.

- Space complexity:
The space complexity is O(k), as we store the substring varray of length k.