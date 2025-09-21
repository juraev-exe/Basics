"""
Tests for the utils module.

This module contains unit tests for all functions in the utils module.
"""

import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import greet, calculate_average, is_even, fibonacci


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""
    
    def test_greet_with_regular_name(self):
        """Test greeting with a regular name."""
        result = greet("Alice")
        expected = "Hello, Alice! Welcome to the Basics project!"
        self.assertEqual(result, expected)
    
    def test_greet_with_empty_string(self):
        """Test greeting with an empty string."""
        result = greet("")
        expected = "Hello, ! Welcome to the Basics project!"
        self.assertEqual(result, expected)


class TestCalculateAverage(unittest.TestCase):
    """Test cases for the calculate_average function."""
    
    def test_calculate_average_with_integers(self):
        """Test average calculation with integer numbers."""
        result = calculate_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)
    
    def test_calculate_average_with_floats(self):
        """Test average calculation with float numbers."""
        result = calculate_average([1.5, 2.5, 3.5])
        self.assertEqual(result, 2.5)
    
    def test_calculate_average_with_mixed_numbers(self):
        """Test average calculation with mixed int and float numbers."""
        result = calculate_average([1, 2.5, 3, 4.5])
        self.assertEqual(result, 2.75)
    
    def test_calculate_average_with_single_number(self):
        """Test average calculation with a single number."""
        result = calculate_average([42])
        self.assertEqual(result, 42.0)
    
    def test_calculate_average_with_empty_list(self):
        """Test that calculate_average raises ValueError with empty list."""
        with self.assertRaises(ValueError) as cm:
            calculate_average([])
        self.assertIn("Cannot calculate average of empty list", str(cm.exception))


class TestIsEven(unittest.TestCase):
    """Test cases for the is_even function."""
    
    def test_is_even_with_even_positive_number(self):
        """Test is_even with positive even numbers."""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(100))
    
    def test_is_even_with_odd_positive_number(self):
        """Test is_even with positive odd numbers."""
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(99))
    
    def test_is_even_with_zero(self):
        """Test is_even with zero."""
        self.assertTrue(is_even(0))
    
    def test_is_even_with_negative_even_number(self):
        """Test is_even with negative even numbers."""
        self.assertTrue(is_even(-2))
        self.assertTrue(is_even(-4))
    
    def test_is_even_with_negative_odd_number(self):
        """Test is_even with negative odd numbers."""
        self.assertFalse(is_even(-1))
        self.assertFalse(is_even(-3))


class TestFibonacci(unittest.TestCase):
    """Test cases for the fibonacci function."""
    
    def test_fibonacci_with_zero(self):
        """Test fibonacci with n=0."""
        result = fibonacci(0)
        self.assertEqual(result, [])
    
    def test_fibonacci_with_one(self):
        """Test fibonacci with n=1."""
        result = fibonacci(1)
        self.assertEqual(result, [0])
    
    def test_fibonacci_with_two(self):
        """Test fibonacci with n=2."""
        result = fibonacci(2)
        self.assertEqual(result, [0, 1])
    
    def test_fibonacci_with_five(self):
        """Test fibonacci with n=5."""
        result = fibonacci(5)
        self.assertEqual(result, [0, 1, 1, 2, 3])
    
    def test_fibonacci_with_ten(self):
        """Test fibonacci with n=10."""
        result = fibonacci(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)
    
    def test_fibonacci_with_negative_number(self):
        """Test that fibonacci raises ValueError with negative n."""
        with self.assertRaises(ValueError) as cm:
            fibonacci(-1)
        self.assertIn("n must be non-negative", str(cm.exception))


if __name__ == '__main__':
    unittest.main()