import unittest
from Python.homework_7_1 import (
    calculate_sum, average, palindrome_checker, custom_sort, find_substring)

class TestCalculateSum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_input = ["2,4,6", "9,7", "1"]
        cls.invalid_input = ["2,4,g", "o,i"]
    
    def setUp(self):
        self.expected_valid = [12, 16, 1]
        self.expected_invalid = ["Не можу це зробити!"]
    
    def test_valid_input(self):
        result = calculate_sum(self.valid_input)
        self.assertEqual(result, self.expected_valid)
    
    def test_invalid_input(self):
        result = calculate_sum(self.invalid_input)
        self.assertEqual(result, self.expected_invalid)

class TestAverage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_input = ["1,3,5", "8,6", "2"]
        cls.invalid_input = ["4,9,g", "o,i"]
    
    def setUp(self):
        self.expected_valid = [3, 7, 2]
        self.expected_invalid = ["Не можу це зробити!"]
    
    def test_valid_input(self):
        result = average(self.valid_input)
        self.assertEqual(result, self.expected_valid)
    
    def test_invalid_input(self):
        result = average(self.invalid_input)
        self.assertEqual(result, self.expected_invalid)

class TestPalindromeChecker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_input = ["121", "33", "2"]
        cls.invalid_input = ["423", "56"]
    
    def setUp(self):
        self.expected_valid = [121, 33, 2]
        self.expected_invalid = ["Не можу це зробити!"]
    
    def test_valid_input(self):
        result = palindrome_checker(self.valid_input)
        self.assertEqual(result, self.expected_valid)
    
    def test_invalid_input(self):
        result = palindrome_checker(self.invalid_input)
        self.assertEqual(result, self.expected_invalid)

class TestCustomSort(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_input = ["5, 2, 3, 1, 4"]
        cls.invalid_input = ["423", "56"]
    
    def setUp(self):
        self.expected_valid = [1, 2, 3, 4, 5]
        self.expected_invalid = ["Не можу це зробити!"]
    
    def test_valid_input(self):
        result = custom_sort(self.valid_input)
        self.assertEqual(result, self.expected_valid)
    
    def test_invalid_input(self):
        result = custom_sort(self.invalid_input)
        self.assertEqual(result, self.expected_invalid)

class TestFindSubstring(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_input = ["Hello, welcome to my world."]
        cls.invalid_input = ["welcome"]
    
    def setUp(self):
        self.expected_valid = ["7"]
        self.expected_invalid = ["Не можу це зробити!"]
    
    def test_valid_input(self):
        result = find_substring(self.valid_input)
        self.assertEqual(result, self.expected_valid)
    
    def test_invalid_input(self):
        result = find_substring(self.invalid_input)
        self.assertEqual(result, self.expected_invalid)

if __name__ == '__main__':
    unittest.main()

