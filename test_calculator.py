#!/usr/bin/env python3
"""
Tests for the calculator module.
Tests pour le module calculateur.
"""

import unittest
import sys
import os

# Add the parent directory to the path to import calculator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import add_numbers, add_list, calculate_addition


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add_numbers_basic(self):
        """Test basic addition of numbers."""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(1, 2, 3, 4), 10)
        self.assertEqual(add_numbers(0), 0)
        self.assertEqual(add_numbers(-5, 5), 0)
        self.assertEqual(add_numbers(1.5, 2.5), 4.0)
    
    def test_add_numbers_single(self):
        """Test addition with single number."""
        self.assertEqual(add_numbers(42), 42)
        self.assertEqual(add_numbers(-10), -10)
        self.assertEqual(add_numbers(3.14), 3.14)
    
    def test_add_numbers_mixed_types(self):
        """Test addition with mixed int and float."""
        self.assertEqual(add_numbers(1, 2.5, 3), 6.5)
        self.assertEqual(add_numbers(10.0, 20), 30.0)
    
    def test_add_numbers_no_args(self):
        """Test that add_numbers raises error with no arguments."""
        with self.assertRaises(ValueError):
            add_numbers()
    
    def test_add_numbers_invalid_types(self):
        """Test that add_numbers raises error with invalid types."""
        with self.assertRaises(TypeError):
            add_numbers(1, "2", 3)
        
        with self.assertRaises(TypeError):
            add_numbers(1, None, 3)
        
        with self.assertRaises(TypeError):
            add_numbers([1, 2])
    
    def test_add_list_basic(self):
        """Test basic list addition."""
        self.assertEqual(add_list([1, 2, 3]), 6)
        self.assertEqual(add_list([0]), 0)
        self.assertEqual(add_list([-1, 1]), 0)
        self.assertEqual(add_list([1.5, 2.5, 3.0]), 7.0)
    
    def test_add_list_empty(self):
        """Test that add_list raises error with empty list."""
        with self.assertRaises(ValueError):
            add_list([])
    
    def test_add_list_invalid_input(self):
        """Test that add_list raises error with invalid input."""
        with self.assertRaises(TypeError):
            add_list("not a list")
        
        with self.assertRaises(TypeError):
            add_list(123)
    
    def test_add_list_invalid_items(self):
        """Test that add_list raises error with invalid list items."""
        with self.assertRaises(TypeError):
            add_list([1, "2", 3])
        
        with self.assertRaises(TypeError):
            add_list([1, None, 3])
    
    def test_calculate_addition_basic(self):
        """Test basic string expression calculation."""
        self.assertEqual(calculate_addition("2+3"), 5)
        self.assertEqual(calculate_addition("1+2+3+4"), 10)
        self.assertEqual(calculate_addition("0+5"), 5)
        self.assertEqual(calculate_addition("10"), 10)
    
    def test_calculate_addition_with_spaces(self):
        """Test expression with spaces."""
        self.assertEqual(calculate_addition("2 + 3"), 5)
        self.assertEqual(calculate_addition(" 1 + 2 + 3 "), 6)
        self.assertEqual(calculate_addition("  5  "), 5)
    
    def test_calculate_addition_floats(self):
        """Test expression with floating point numbers."""
        self.assertEqual(calculate_addition("1.5+2.5"), 4.0)
        self.assertEqual(calculate_addition("3.14+0.86"), 4.0)
        self.assertEqual(calculate_addition("1.5+2+0.5"), 4)  # Result should be int if whole
    
    def test_calculate_addition_invalid_expression(self):
        """Test invalid expressions."""
        with self.assertRaises(ValueError):
            calculate_addition("")
        
        with self.assertRaises(ValueError):
            calculate_addition("2++3")
        
        with self.assertRaises(ValueError):
            calculate_addition("+2+3")
        
        with self.assertRaises(ValueError):
            calculate_addition("2+3+")
        
        with self.assertRaises(ValueError):
            calculate_addition("2*3")  # Multiplication not allowed
        
        with self.assertRaises(ValueError):
            calculate_addition("2-3")  # Subtraction not allowed
        
        with self.assertRaises(ValueError):
            calculate_addition("2+3-1")  # Mixed operations not allowed
    
    def test_calculate_addition_invalid_type(self):
        """Test with non-string input."""
        with self.assertRaises(TypeError):
            calculate_addition(123)
        
        with self.assertRaises(TypeError):
            calculate_addition([1, 2, 3])
    
    def test_large_numbers(self):
        """Test with large numbers."""
        self.assertEqual(add_numbers(1000000, 2000000), 3000000)
        self.assertEqual(add_list([999999, 1]), 1000000)
        self.assertEqual(calculate_addition("1000000+2000000"), 3000000)
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(add_numbers(-5, -10), -15)
        self.assertEqual(add_list([-1, -2, -3]), -6)
        # Note: calculate_addition doesn't support negative numbers in current implementation
        # as minus sign would be interpreted as subtraction
    
    def test_zero_combinations(self):
        """Test various zero combinations."""
        self.assertEqual(add_numbers(0, 0, 0), 0)
        self.assertEqual(add_list([0, 5, 0]), 5)
        self.assertEqual(calculate_addition("0+0+5"), 5)


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)