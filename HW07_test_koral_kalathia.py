from typing import Tuple, List
import unittest
from HW07_koral_kalathia import anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer


class HW07_Testcases(unittest.TestCase):
    """This class contains all test cases for all the functions"""

    def test_anagrams_lst(self):
        """Function is used to test the function : anagrams_lst"""
        self.assertEqual(anagrams_lst("", ""), True)
        self.assertNotEqual(anagrams_lst("iceman", "cinemaa"), True)
        self.assertEqual(anagrams_lst("cinema", "Iceman"), True)
        self.assertEqual(anagrams_lst("dormitory", "dirtyroom"), True)
        self.assertEqual(anagrams_lst("Koral", "larok"), True)

    def test_anagrams_dd(self):
        """Function is used to test the function : anagrams_dd"""
        self.assertEqual(anagrams_dd("", ""), True)
        self.assertNotEqual(anagrams_dd("iceman", "cinemaa"), True)
        self.assertEqual(anagrams_dd("Iceman", "CinemA"), True)
        self.assertEqual(anagrams_dd("dormitory", "dirtyroom"), True)
        self.assertEqual(anagrams_dd("Koral", "LaroK"), True)

    def test_anagrams_cntr(self):
        """Function is used to test the function : anagrams_cntr"""
        self.assertEqual(anagrams_cntr("", ""), True)
        self.assertNotEqual(anagrams_cntr("iCeman", "Cinemaa"), True)
        self.assertEqual(anagrams_cntr("Cinema", "icemaN"), True)
        self.assertEqual(anagrams_cntr("dormitory", "dirtyroom"), True)
        self.assertEqual(anagrams_cntr("Koral", "LAroK"), True)

    def test_covers_alphabet(self):
        """Function is used to test the function : covers_alphabet"""
        self.assertTrue(covers_alphabet("abcdefghijklmnopqrstuvwxyz"), True)
        self.assertEqual(covers_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc"), True)
        self.assertEqual(covers_alphabet("We promptly judged antique ivory buckles for the next prize"), True)
        self.assertNotEqual(covers_alphabet("We promptly judged ivory buckles for the next prize"), True)
        self.assertEqual(covers_alphabet("The quick, brown, fox; jumps over the lazy dog!"), True)

    def test_web_analyzer(self):
        """Function is used to test the funvtion :  web_analyzer"""
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com')]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
