class Stack:
    def __init__(self):
        self._stack = []

    # public methods declaration
    def push(self, item):
        """Push an item onto the stack."""
        self._stack.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self._stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self._stack[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self._stack)

    def sort(self):
        """Sort the stack using in-place quicksort."""
        if not self.is_empty():
            self._quicksort(self._stack)

    def display(self):
        """Display all elements in the stack."""
        print(self._stack)

    # private methods declaration
    def _quicksort(self, stack_list, low=0, high=None):
        """Simplified quicksort algorithm for in-place sorting."""
        if high is None:
            high = len(stack_list) - 1  # Initialize high if not provided.

        if low < high:
            pivot_index = self._partition(stack_list, low, high)
            
            self._quicksort(stack_list, low, pivot_index - 1)
            self._quicksort(stack_list, pivot_index + 1, high)
    
    def _partition(self, stack_list, low, high):
        """Partition the list and return the pivot index."""
        pivot = stack_list[high]
        i = low - 1

        for j in range(low, high):
            if stack_list[j] <= pivot:
                i += 1
                stack_list[i], stack_list[j] = stack_list[j], stack_list[i]
        
        stack_list[i + 1], stack_list[high] = stack_list[high], stack_list[i + 1]
        
        # Return the partition index.
        return i + 1
