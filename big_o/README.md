Big O notation is a mathematical representation that describes the efficiency or performance of an algorithm in terms of time or space complexity as the input size grows. It characterizes an algorithm's behavior, particularly its growth rate, which helps in comparing and predicting performance.

### Common Big O Notations

1. **O(1) - Constant Time Complexity:**
   - The algorithm's runtime remains constant regardless of the input size.
   - Example: Accessing an element in an array by index.
  
2. **O(log n) - Logarithmic Time Complexity:**
   - The runtime increases logarithmically as the input size grows.
   - Common in algorithms that halve the problem size each time, like binary search.

3. **O(n) - Linear Time Complexity:**
   - The runtime grows linearly with the input size.
   - Example: Iterating through an array once.

4. **O(n log n) - Linearithmic Time Complexity:**
   - Slightly more complex than linear, common in efficient sorting algorithms.
   - Example: Merge sort, quicksort (average case).

5. **O(n²) - Quadratic Time Complexity:**
   - The runtime grows proportionally to the square of the input size.
   - Example: Nested loops in a bubble sort for an array. 

6. **O(n³) - Cubic Time Complexity:**
   - The runtime grows proportionally to the cube of the input size.
   - Example: Triple nested loops, often found in certain matrix operations.

7. **O(2ⁿ) - Exponential Time Complexity:**
   - The runtime doubles with each additional element in the input.
   - Example: Recursive algorithms for the Fibonacci sequence, brute-force combinatorial problems.

8. **O(n!) - Factorial Time Complexity:**
   - The runtime grows factorially with the input size.
   - Example: Generating all permutations of a list.

### Using Big O Notation

Big O notation provides a way to analyze algorithms for:
- **Best Case** (optimistic scenario)
- **Worst Case** (pessimistic scenario)
- **Average Case** (expected behavior for random input)