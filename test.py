import io
import sys
import unittest
from main import (
    search_char_in_string,
    check_is_palindrome,
    check_duplicates,
    deduplicate,
    check_are_anagrams,
    get_largest_prime_factor,
    check_is_pandigital,
    sort_numbers
)

class TestMyFunctions(unittest.TestCase):
    def test_search_char_in_string(self):
        self.assertEqual(search_char_in_string('a', 'banana'), 1)
        self.assertEqual(search_char_in_string('z', 'banana'), -1)


    def test_check_is_palindrome(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        check_is_palindrome('Rad ar')
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output.strip(), 'Palindrome')

        captured_output = io.StringIO()
        sys.stdout = captured_output
        check_is_palindrome('hello')
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output.strip(), 'Not palindrome')

        captured_output = io.StringIO()
        sys.stdout = captured_output
        check_is_palindrome('')
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output.strip(), 'Empty string')


    def test_check_duplicates(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        check_duplicates(['apple', 'banana', 'apple'])
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output.strip(), 'Contains duplicates')

        captured_output = io.StringIO()
        sys.stdout = captured_output
        check_duplicates(['apple', 'banana', 'orange'])
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output.strip(), 'Does not contain duplicates')


    def test_deduplicate(self):
        self.assertEqual(deduplicate(['apple', 'banana', 'apple', 'orange']), ['apple', 'banana', 'orange'])


    def test_check_are_anagrams(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        check_are_anagrams('listen', 'silent')
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output.strip(), 'Anagram')

        captured_output = io.StringIO()
        sys.stdout = captured_output
        check_are_anagrams('hello', 'world')
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output.strip(), 'Not anagram')


    def test_get_largest_prime_factor(self):
        self.assertEqual(get_largest_prime_factor(78), 13)


    def test_check_is_pandigital(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        check_is_pandigital(15234)
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output.strip(), 'Pandigital')

        captured_output = io.StringIO()
        sys.stdout = captured_output
        check_is_pandigital(34121)
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output.strip(), 'Not pandigital')


    def test_sort_numbers(self):
        self.assertEqual(sort_numbers([4, 3, 2, 1]), [1, 2, 3, 4])

unittest.main()