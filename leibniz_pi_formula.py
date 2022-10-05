"""
An implementation of the Leibniz formula for Pi.

For manual testing:
python leibniz_pi_formula.py
"""


def pi(terms: int) -> float:
    """Implementation of the Leibniz formula for Pi."""
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0

    for _ in range(terms):
        pi += operation * (numerator/denominator)

        denominator += 2.0
        operation *= -1.0

    return pi


if __name__ == '__main__':
    terms = input('Enter the number of terms: ').strip()
    terms = int(terms)

    print(f'{pi(terms)=}')
