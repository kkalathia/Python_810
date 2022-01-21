import unittest
from typing import List
from HW05_koral_kalathia import get_lines, reverse, substring, find_second


class Reverse(unittest.TestCase):
    def test_reverse(self) -> bool:
        """ Verifies if reverse function reverses the string properly"""
        self.assertTrue(reverse("koral") == "larok")
        self.assertFalse(reverse("abcabc") == "abcabc")
        self.assertTrue(reverse("abcabc") == "cbacba")
        self.assertTrue(reverse("12345678") == "87654321")
        self.assertTrue(reverse("") == "")


class Substring(unittest.TestCase):
    def test_substring(self) -> bool:
        """Verifies if function returns the correct index of substring"""
        self.assertTrue(substring("aab", "babaab") == 3)
        self.assertTrue(substring("abc", "bcacab") == -1)
        self.assertTrue(substring("", "bcacab") == -1)
        self.assertFalse(substring("abc", "asdfghjabc") == 0)


class FindSecond(unittest.TestCase):
    def test_find_second(self) -> bool:
        """Verifies if the function returns the correct index
        of second occurence of substring
        """
        self.assertTrue(find_second("aab", "babaabaab") == 6)
        self.assertTrue(find_second("", "bcacab") == -1)
        self.assertTrue(find_second("han", "rohan") == -1)
        self.assertFalse(find_second("abc", "abcbbabc") == 0)


class GetLinesTest(unittest.TestCase):
    def test_get_lines(self) -> bool:
        """
        The function reads the file combine lines that end with a backslash
        with the subsequent line or lines until a line is found that does not
        end with a backslash
        """
        file_name = "part_4_test.txt"
        expect: List[str] = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>',
                             '<line5>', '<line6>']
        result: List[str] = list(get_lines(file_name))
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
