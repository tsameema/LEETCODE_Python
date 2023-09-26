## Intuition
The problem asks us to find the elements that are present in one list but not in the other. To solve this, we can use a straightforward approach where we iterate through both lists and check for each element if it exists in the other list. If an element is present in one list but not in the other, we add it to a separate list for each input list. This way, we can keep track of the elements that are unique to each list.
## Approach
1. Initialize two empty lists, list1_2 to keep track of elements unique to nums1 and nums2.
2. Iterate through the unique elements of nums1 using a set to avoid duplicates.
    - For each element n1, check if it is not present in nums2.     
    - If it's not, append it to list1_2[0].
3. Similarly, iterate through the unique elements of nums2.
    - For each element n2, check if it is not present in nums1.     
    - If it's not, append it to list1_2[1].
4. After iterating through both lists, list1_2 will contain two sublists: one for elements unique to nums1 and the other for elements unique to nums2.
5. Return list1_2.

## Complexity
- Time complexity:
The time complexity of this approach is dominated by the set operations and the iterations through the unique elements of nums1 and nums2. Let n be the length of the longer list between nums1 and nums2. The time complexity is $O(n)$ because we iterate through both lists once and use set operations, which typically have a time complexity of O(n) for insertion and lookup.

- Space complexity:
The space complexity is $O(n)$ because we store the unique elements in sets and maintain two separate lists for elements unique to nums1 and nums2.