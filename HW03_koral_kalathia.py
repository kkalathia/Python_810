class Fraction:
    """ Support addition, subtraction, multiplication, division, equality, non equality, less than, greater than, less than equal, greater than equal of fractions
        with a simple algorithm
    """

    def __init__(self, num: float, denom: float) -> None:
        """ store num and denom
            Raise ZeroDivisionError on 0 denominator
        """
        self.num: float = num
        self.denom: float = denom
        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be 0")

    def __str__(self) -> str:
        """ return a String to display fractions """
        return f"{self.num}/{self.denom}"

    def __add__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        return Fraction(self.num * other.num, self.denom * other.denom)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """ Divide two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        return Fraction(self.num * other.denom, self.denom * other.num)

    def __eq__(self, other: "Fraction") -> bool:
        """ Check equality between  two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        if ((self.num * other.denom) == (self.denom * other.num)) :
            return True
        else:
            return False

    def __ne__(self, other: "Fraction") -> bool:
        """ Check not equal to between two fractions using simplest approach.
                    Calculate new numerator and denominator and return new Fraction
                """
        if ((self.num * other.denom) != (self.denom * other.num)):
            return True
        else:
            return False

    def __lt__(self, other: "Fraction") -> bool:
        """ Check less than two fractions using simplest approach.
         Calculate new numerator and denominator and return new Fraction
        """
        if ((self.num * other.denom) < (self.denom * other.num)):
            return True
        else:
            return False

    def __le__(self, other: "Fraction") -> bool:
        """ Check less than equal two fractions using simplest approach.
         Calculate new numerator and denominator and return new Fraction
        """
        if ((self.num * other.denom) <= (self.denom * other.num)):
            return True
        else:
            return False

    def __gt__(self, other: "Fraction") -> bool :
        """ Check greater than between two fractions using simplest approach.
         Calculate new numerator and denominator and return new Fraction
        """
        if ((self.num * other.denom) > (self.denom * other.num)):
            return True
        else:
            return False

    def __ge__(self, other: "Fraction") -> bool:
        """ Check greater than equal between two fractions using simplest approach.
         Calculate new numerator and denominator and return new Fraction
        """
        if ((self.num * other.denom) <= (self.denom * other.num)):
            return True
        else:
            return False

    def simplify(self):
        """Use to simplify the fraction"""
        a:float = self.num
        b:float = self.denom
        i:int = 1
        while (i <= a and i <= b):
            if (a % i == 0 and b % i == 0):
                gcd:int = i
            i = i + 1
        num:float = a / gcd
        denom:float = b / gcd
        return Fraction(int(num), int(denom))


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

        num: float = get_number("Enter the Numerator:")
        denom: float = get_number("Enter the Denominator:")
        try:
            return Fraction(num, denom)
        except:
            print("Denominator can't be 0")
        # TODO: use the same approach as get_number() to retrieve
        # TODO: an instance of class Fraction


def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    okay: bool = True
    result: Fraction  # just define the type of result, don't set a value

    if operator == '+':
        result = f1 + f2
    elif operator == '-':
        result = f1 - f2
    elif operator == '*':
        result = f1 * f2
    elif operator == '/':
        result = f1 / f2
    elif operator == '=':
        result = f1 == f2
    elif operator == '!=':
        result = f1 != f2
    elif operator == '>':
        result = f1 > f2
    elif operator == '>=':
        result = f1 >= f2
    elif operator == '<':
        result = f1 < f2
    elif operator == '<=':
        result = f1 <= f2
    else:
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False

    if okay:
        print(f"{f1} {operator} {f2} = {result}")


def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!')
    f1: Fraction = get_fraction()
    operator: str = input("Operation (+, -, *, /, =, !=, <, <=, >=, >): ")
    f2: Fraction = get_fraction()

    try:
        compute(f1, operator, f2)
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    main()