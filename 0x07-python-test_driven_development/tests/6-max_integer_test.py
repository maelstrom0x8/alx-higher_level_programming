#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    
    def test_empty_list(self):
        """Test an empty list. Should return None."""
        self.assertIsNone(max_integer([]))

    def test_string(self):
        """Test a string. Should return 'o' (maximum character
        based on ASCII value)."""
        self.assertEqual(max_integer('Klingon'), 'o')

    def test_single_element_list(self):
        """Test a list with a single element. Should return
        the element itself."""
        self.assertEqual(max_integer([5]), 5)

    def test_string_list(self):
        """Test a list of strings. Should return the string with
        the maximum lexicographic order."""
        strings = ["Saru", "is", "coming", "today"]
        self.assertEqual(max_integer(strings), "today")

    def test_nonnegative_numbers(self):
        """Test a list of positive integers. Should return the
        maximum integer."""
        self.assertEqual(max_integer([3, 6, 1, 8, 2]), 8)

    def test_ints_and_floats(self):
        """Test a list of integers and floats. Should return
        the maximum number."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_mixed_positive_and_negative_numbers(self):
        """Test a list of mixed positive and negative integers.
        Should return the maximum integer."""
        self.assertEqual(max_integer([-3, 6, -1, 8, -2]), 8)

    def test_one_element_list(self):
        """Test a list with a single element. Should
        return the element itself."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_float_numbers(self):
        """Test a list of positive float numbers.
        Should return the maximum float number."""
        self.assertEqual(max_integer([3.5, 2.7, 4.8, 1.2]), 4.8)

    def test_unordered_list(self):
        """Test an unordered list of integers. Should
        return the maximum integer."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_mixed_integer_and_float_numbers(self):
        """Test a list of mixed integers and floats.
        Should return the maximum number."""
        self.assertEqual(max_integer([3, 2.7, 4, 1.2]), 4)

    def test_empty_string(self):
        """Test an empty string. Should return None."""
        self.assertEqual(max_integer(""), None)

    def test_empty_list(self):
        """Test an empty list. Should return None."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_large_numbers(self):
        """Test a list of large positive integers.
        Should return the maximum integer."""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_large_negative_numbers(self):
        """Test a list of large negative integers.
        Should return the maximum integer."""
        self.assertEqual(max_integer([-1000000, -999999, -1000001]), -999999)

    def test_max_at_beginning(self):
        """Test a list with a maximum value at the
        beginning. Should return the maximum integer."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_mixed_large_numbers(self):
        """Test a list of mixed large numbers.
        Should return the maximum integer."""
        self.assertEqual(max_integer([1000000, -999999, 1000001]), 1000001)


    def test_ordered_list(self):
        """Test an ordered list of integers.
        Should return the maximum integer."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_negative_numbers(self):
        """Test a list of negative integers.
        Should return the maximum integer."""
        self.assertEqual(max_integer([-3, -6, -1, -8, -2]), -1)


    def test_floats(self):
        """Test a list of positive floats. Should return
        the maximum float number."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)




if __name__ == '__main__':
    unittest.main()
