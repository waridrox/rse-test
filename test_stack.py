import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def test_stack_functionality(self):
        """Testing the functionality of the Stack class."""
        stack = Stack()

        # Test for pushing elements
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.size(), 2, "Stack size should be 2 after two pushes")
        self.assertEqual(stack.peek(), 20, "Top element should be 20 after pushing 10 and 20")

        # Test for popping elements
        self.assertEqual(stack.pop(), 20, "Popped element should be 20")
        self.assertEqual(stack.size(), 1, "Stack size should be 1 after one pop")
        self.assertEqual(stack.peek(), 10, "Top element should be 10 after popping 20")

        # Test forr sorting the stack
        stack.push(5)
        stack.push(15)
        stack.sort()  # Sorting the stack
        self.assertEqual(stack._stack, [5, 10, 15], "Stack should be sorted to [5, 10, 15]")

        # Test for popping all elements
        stack.pop()  # Pop 15
        stack.pop()  # Pop 10
        stack.pop()  # Pop 5
        self.assertTrue(stack.is_empty(), "Stack should be empty after popping all elements")

        # Test popping from an empty stack
        with self.assertRaises(IndexError, msg="Pop from an empty stack should raise IndexError"):
            stack.pop()

        # Test peeking from an empty stack
        with self.assertRaises(IndexError, msg="Peek from an empty stack should raise IndexError"):
            stack.peek()


if __name__ == '__main__':
    unittest.main()
