#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Implement a class for fractions that supports addition, subtraction, multiplication, and division """


class Fraction:
    """ Support addition, subtraction, multiplication, and division of fractions
        with a simple algorithm
    """

    def __init__(self, num: float, denom: float) -> None:
        """ store num and denom
            Raise ZeroDivisionError on 0 denominator
        """
        self.num: float = num
        self.denom: float = denom
        if denom == 0:
            raise ValueError("The Denominator cannot be 0, Please try again")
        # TODO: implement me

    def __str__(self) -> str:
        """ return a String to display fractions """
        return str(self.num) + '/' + str(self.denom)
        # TODO: implement me

    def plus(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)

        # TODO: implement me

    def minus(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)
        # TODO: implement me

    def times(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        return Fraction(self.num * other.num, self.denom * other.denom)
        # TODO: implement me

    def divide(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        return Fraction(self.num * other.denom, self.denom * other.num)
        # TODO: implement me

    def equal(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are equivalent """
        if self.num * other.denom == self.denom * other.num:
            return True
        else:
            return False
        # TODO: implement me


def test_suite() -> None:
    """ We'll see a better testing approach next week but here's a start.
        Note that each statement includes the result of the computation plus
        the expected answer to help to quickly identify if everything works properly.
    """
    f12: Fraction = Fraction(1, 2)
    f34: Fraction = Fraction(3, 4)
    f68: Fraction = Fraction(6, 8)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    f912: Fraction = Fraction(9, 12)
    f44: Fraction = Fraction(4, 4)
    f48: Fraction = Fraction(4, 8)

    print(f"{f12} + {f34} = {f12.plus(f34)} [10/8]")
    print(f"{f12} * {f68} = {f12.times(f68)} [6/16]")
    print(f"{f12} * {f32} = {f12.times(f32)} [3/4]")

    # print("Testing the test Function!!")
    # include a test with three operands
    print(f"{f12} + {f34} + {f44} = {f12.plus(f34).plus(f44)} [72/32]")




    # TODO: Be sure to test all methods, including __str__


def get_number(prompt: str) -> float:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")


def get_fraction() -> Fraction:
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:

        num: float = (get_number("Enter the Value for Numerator:"))
        denom: float = (get_number("Enter the Denominator:"))
        try:
            return Fraction(num, denom)
        except ValueError:
            print("The Denominator can not be 0")
        # TODO: use the same approach as get_number() to retrieve
        # TODO: an instance of class Fraction


def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    okay: bool = True
    result: Fraction  # just define the type of result, don't set a value

    if operator == '+':
        result = f1.plus(f2)
    elif operator == '-':
        result = f1.minus(f2)
    elif operator == '*':
        result = f1.times(f2)
    elif operator == '/':
        result = f1.divide(f2)
    elif operator == '=':
        result = f1.equal(f2)
    else:
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False

    if okay:
        print(f"{f1} {operator} {f2} = {result}")


def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!')
    f1: Fraction = get_fraction()
    operator: str = input("Operation (+, -, *, /, =): ")
    f2: Fraction = get_fraction()

    try:
        compute(f1, operator, f2)
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    test_suite()
    main()
