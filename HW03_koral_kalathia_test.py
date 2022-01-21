import unittest
from HW03_koral_kalathia import Fraction

class TestFraction(unittest.TestCase):
    """ test class Fraction """
    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f: Fraction = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.denom, 4)

    def test_init_exception(self):
        """ verify that ZeroDivisionError is raised when appropriate """
        with self.assertRaises(ZeroDivisionError): Fraction(10, 0)

    def test_simplify(self):
        """Use to verify simplified version of fraction"""
        self.assertEqual(Fraction(9, 12).simplify(), Fraction(3, 4))
        self.assertEqual(Fraction(1, 2).simplify(), Fraction(1, 2))
        self.assertEqual(str(Fraction(1, 2).simplify()), str(Fraction(1, 2)))

    def test_str(self):
        """ verify String in Fraction"""
        f66: Fraction = Fraction(6, 6)
        f24: Fraction = Fraction(2, 4)
        self.assertEqual(str(f66), "6/6")
        self.assertNotEqual(str(f24), "8/6")
        self.assertTrue(str(f24), "2/4")

    def test_add(self):
        """ verify Fraction addition """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 + f34, Fraction(10, 8))

    def test_sub(self):
        """ verify Fraction Subtraction """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 - f34, Fraction(-1, 4))

    def test_mul(self):
        """ verify Fraction Multiplication """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 * f34, Fraction(3, 8))

    def test_truediv(self):
        """ verify Fraction Division """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 / f34, Fraction(4, 6))

    def test_eq(self):
        """ verify Fraction Equality """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f48: Fraction = Fraction(4, 8)
        self.assertTrue(f12 == f12)
        self.assertFalse(f12 == f34)
        self.assertTrue(f12 == f48)


    def test_ne(self):
        """ verify Fraction Not Equal """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f48: Fraction = Fraction(4, 8)
        self.assertTrue(f12 != f34)
        self.assertFalse(f12 != f48)
        self.assertFalse(f12 != f12)

    def test_lt(self):
        """ verify Fraction Less than """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)
        self.assertTrue(f12 < f34)
        self.assertFalse(f44 < f12)

    def test_le(self):
        """ verify Fraction LessThan Equal to """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f48: Fraction = Fraction(4, 8)
        f66: Fraction = Fraction(6, 6)
        self.assertTrue(f12 <= f34)
        self.assertTrue(f12 <= f48)
        self.assertFalse(f66 <= f12)

    def test_gt(self):
        """ verify Fraction Greater than """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f105: Fraction = Fraction(10, 5)
        self.assertTrue(f34 > f12)
        self.assertFalse(f12 > f105)
        self.assertFalse(f12 > f12)

    def test_ge(self):
        """ verify Fraction Greater than Equal """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f93: Fraction = Fraction(9, 3)
        f124: Fraction = Fraction(12, 4)
        self.assertTrue(f12 >= f34)
        self.assertTrue(f93 >= f124)
        self.assertFalse(f93 >= f12)

    def test_3_operands(self):
        """ verify expressions with more than two operands """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)
        f84: Fraction = Fraction(8, 4)
        f48: Fraction = Fraction(4, 8)
        f816: Fraction = Fraction(8, 16)
        self.assertTrue(f12 + f34 + f44 == Fraction(72, 32))
        self.assertTrue(f12 - f34 - f44 == Fraction(-5,4))
        self.assertTrue(f12 * f34 * f44 == Fraction(3, 8))
        self.assertTrue(f12 / f34 / f44 == Fraction(4, 6))
        self.assertTrue(f12 == f48 == f816)
        self.assertFalse(f12 == f816 == f34)
        self.assertTrue(f12 != f34 != f44)
        self.assertFalse(f12 != f48 != f816)
        self.assertTrue(f12 < f34 < f44)
        self.assertFalse(f84 < f44 < f12)
        self.assertTrue(f12 <= f12 <= f48)
        self.assertFalse(f84 <= f44 < f12)
        self.assertTrue(f44 > f34 > f12)
        self.assertFalse(f12 > f44 > f84)
        self.assertTrue(f12 >= f48 >= f816)
        self.assertFalse(f12 >= f44 >= f816)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)