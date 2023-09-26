## Intuition
The problem asks us to find the product of all elements in an array except the current element at each index. One way to approach this problem is to calculate the product of all elements to the left of each element and the product of all elements to the right of each element. Then, we can multiply these left and right products to get the final result. To optimize the space complexity, we can use two arrays, one for the left products and one for the right products.

## Approach
1. Initialize two arrays, left and right, both of the same length as the input nums. These arrays will store the product of all elements to the left and right of each element in nums.

2. Initialize two variables, left_product and right_product, to 1. These variables will keep track of the running product as we iterate through the nums array from left to right and right to left, respectively.

3. Iterate through nums from left to right and update the left array and left_product as follows:

    - For each element at index n, set left[n] to be equal to left_product.
    - Update left_product by multiplying it with the current element nums[n].
4. Iterate through nums from right to left and update the right array and right_product as follows:

   - each element at index n, set right[n] to be equal to right_product.
    - Update right_product by multiplying it with the current element nums[n].
5. Finally, create a prod_list by multiplying the corresponding elements from the left and right arrays for each index in nums. This prod_list will contain the product of all elements except the current element at each index.

6. Return the prod_list as the result.
## Complexity
### - Time complexity:
$O(n)$ where n is the length of the input nums. We iterate through nums twice, once from left to right and once from right to left, performing constant time operations in each iteration.

### - Space complexity:
$O(n)$ where n is the length of the input nums. We use two additional arrays, left and right, of the same length as nums to store the left and right products.