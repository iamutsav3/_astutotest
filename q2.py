"""
Q2: Compressed Stack Length

You are processing a stream of numbers one by one.

Sometimes, a number cancels itself out if it immediately follows the same number
that is still active.

As you read the numbers from **left to right**:
- If the current number cancels out the most recent active number, both disappear.
- Otherwise, the number remains active.

After the entire list has been processed, determine how many numbers are still
active.

Return this final count.

Examples:
---------
Input: [1, 2, 2, 3]  → Output: 2
  Process: 1 → [1]
           2 → [1, 2]
           2 → [1]      (2 cancels with previous 2)
           3 → [1, 3]
  Final count: 2

Input: [4, 4, 4, 4]  → Output: 0
  Process: 4 → [4]
           4 → []      (cancels)
           4 → [4]
           4 → []      (cancels)
  Final count: 0

Input: [1, 1, 2, 2, 1]  → Output: 1
  Process: 1 → [1]
           1 → []      (cancels)
           2 → [2]
           2 → []      (cancels)
           1 → [1]
  Final count: 1

Input: []  → Output: 0
"""


def compressed_stack_length(lst):
    """
    Calculate the number of elements remaining after cancellations.

    Process the list from left to right. When a number matches the most recent
    active number, both are removed. Otherwise, the number is added.

    Args:
        lst (list): List of integers

    Returns:
        int: Count of numbers remaining after all cancellations

    Examples:
        >>> compressed_stack_length([1, 2, 2, 3])
        2
        >>> compressed_stack_length([4, 4, 4, 4])
        0
        >>> compressed_stack_length([])
        0
    """
    # TODO: Implement your solution here
       

   
def compressed_stack_length(lst):
    stack = []

    for num in lst:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)

    return len(stack)




if __name__ == "__main__":
    # Test your solution here
    print(compressed_stack_length([1, 2, 2, 3]))    # Should print: 2
    print(compressed_stack_length([4, 4, 4, 4]))    # Should print: 0
    print(compressed_stack_length([]))              # Should print: 0
