import argparse
import sys

import sympy
from sympy import Number

def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f",
        "--function",
        type=str,
        required=True,
        help="Function to aproximate",
    )

    parser.add_argument(
        "-a",
        "--at",
        type=str,
        required=False,
        help="Point to aproximate around",
    )

    parser.add_argument(
        "-x",
        type=str,
        required=False,
        help="Value of the function to aproximate",
    )

    parser.add_argument(
        "-d",
        "--derivatives",
        type=Number,
        default=5,
        help="Maximum degree of the derivatives to use for the aproximation",
    )

    args = parser.parse_args()

    function = sympy.sympify(args.function)

    taylor = 0
    x, a = sympy.symbols("x a")

    taylor_func = function.subs(x, a)

    for i in range(0, args.derivatives):
        diff = sympy.diff(taylor_func, a, i) / sympy.factorial(i)
        taylor += diff * (x - a) ** i

    taylor = sympy.simplify(taylor)

    if args.at is not None:
        taylor = taylor.subs(a, sympy.sympify(args.at))
    if args.x is not None:
        taylor = taylor.subs(x, sympy.sympify(args.x))

    print(taylor)

    # print(sympy.diff("e^x", "x", 2))

if __name__ == "__main__":
    main()
