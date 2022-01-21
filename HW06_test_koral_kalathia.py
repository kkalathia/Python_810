import unittest
from HW06_koral_kalathia1 import list_difference, list_intersect, list_copy, remove_vowels, check_pwd, DonutQueue


class MyTestCase(unittest.TestCase):

    def test_list_copy(self):
        """Function is used to test copy of list"""
        self.assertEqual(list_copy([7, 8, 9, 10]), [7, 8, 9, 10])
        self.assertEqual(list_copy(["Rohan", "6,7,8", 7]), ["Rohan", "6,7,8", 7])
        self.assertEqual(list_copy([]), [])
        self.assertNotEqual(list_copy([10, 11, 12, 13]), [])
        self.assertNotEqual(list_copy([10, 11, 12, 13]), [10, 12])

    def test_list_intersect(self):
        """Function is used to test intersection between two lists"""
        self.assertEqual(list_intersect([1, 2, 3], ["a", "b", "c"]), [])
        self.assertEqual(list_intersect(["a", "b", "c"], ["a", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(list_intersect([1, 2, 3], [1, 2, 3]), [1, 2, 3])
        self.assertNotEqual(list_intersect([1, 2, 3], [2, 3, 4]), [1, 4])

    def test_list_difference(self):
        """Function is used to test differences between two list"""
        self.assertNotEqual(list_difference([5, 6, 7], ["d", "e", "f"]), [5, 6, 7, "d", "e", "f"])
        self.assertNotEqual(list_difference(["a", "b", "c"], ["a", "b", "c"]), ["a", "b", "c"])
        self.assertNotEqual(list_difference([1, 2, 3], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(list_difference([1, 2, 3], [2, 3, 4]), [1])

    def test_remove_vowels(self):
        """Function is used to test remove_vowels"""
        self.assertEqual(remove_vowels("I am Koral Kalathia"), "Koral Kalathia")
        self.assertEqual(remove_vowels("My best friend is pooh"), "My best friend pooh")
        self.assertEqual(remove_vowels("Hey I am koral"), "Hey koral")
        self.assertNotEqual(remove_vowels("sinchan is a boy"), "is boy")

    def test_check_pwd(self):
        """Function is used to test check_pwd"""
        self.assertEqual(check_pwd('1KoralK'), True)
        self.assertEqual(check_pwd('1Koral'), False)
        self.assertEqual(check_pwd('2'), False)
        self.assertNotEqual(check_pwd('5Bbcsdd'), True)


class DonutQueueTest(unittest.TestCase):
    def test_queue(self):
        dq = DonutQueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Sujit", False)
        dq.arrive("Fei", False)
        dq.arrive("Prof JR", True)
        self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
        dq.arrive("Nanda", True)
        self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(dq.next_customer(), "Prof JR")
        self.assertEqual(dq.next_customer(), "Nanda")
        self.assertEqual(dq.next_customer(), "Sujit")
        self.assertEqual(dq.waiting(), "Fei")
        self.assertEqual(dq.next_customer(), "Fei")
        self.assertIsNone(dq.next_customer())


if __name__ == '__main__':
    unittest.main()
