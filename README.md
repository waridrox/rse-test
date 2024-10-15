# Stack implementation - rse@bath

This document describes the `Stack` class and provides usage instructions, including testing procedures.

---

## Overview

The `Stack` class implements a basic Last-In-First-Out (LIFO) stack with common stack operations such as pushing, popping, peeking, sorting, and checking the size of the stack.

---

## Public Methods

### `push(item)`
- **Description**: Pushes an item onto the stack.
- **Parameters**: 
  - `item`: The element to push onto the stack.
- **Returns**: None.

### `pop()`
- **Description**: Removes and returns the top item from the stack.
- **Returns**: The top element.
- **Raises**: `IndexError` if the stack is empty.

### `peek()`
- **Description**: Returns the top item without removing it.
- **Returns**: The top element.
- **Raises**: `IndexError` if the stack is empty.

### `is_empty()`
- **Description**: Checks if the stack is empty.
- **Returns**: `True` if the stack is empty, `False` otherwise.

### `size()`
- **Description**: Returns the number of elements in the stack.
- **Returns**: The size of the stack.

### `sort()`
- **Description**: Sorts the stack in ascending order using the quicksort algorithm.
- **Returns**: None.

### `display()`
- **Description**: Displays the elements of the stack.
- **Returns**: None.

---

## Private Methods

### `_quicksort(stack_list, low=0, high=None)`
- **Description**: Private helper method to sort the stack using the quicksort algorithm.
- **Returns**: None.

### `_partition(stack_list, low, high)`
- **Description**: Private helper function for the quicksort algorithm that partitions the list.
- **Returns**: The index of the pivot.

---

## Testing

To test the functionality of the `Stack` class, we can use Python's built-in `unittest` framework. All the tests are defined in the `test_stack.py` file.

### Running the Tests

Run the following command to execute the tests:

```bash
python -m unittest test_stack.py
