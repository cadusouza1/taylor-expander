import argparse
from itertools import count
from typing import Any, Generator

import sympy
from sympy import Expr, Number, Symbol


def taylor_generator(f, x: Symbol, a: Symbol) -> Generator[Any, Expr, Any]:
    taylor_func = f.subs(x, a)

    for i in count(0):
        yield taylor_func * (x - a) ** i / sympy.factorial(i)
        taylor_func = taylor_func.diff(a)


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

    x, a = sympy.symbols("x a")

    taylor = 0
    for i, taylor_term in enumerate(taylor_generator(function, x, a)):
        if i > args.derivatives - 1:
            break

        taylor += taylor_term

    taylor = sympy.simplify(taylor)

    if args.at is not None:
        taylor = taylor.subs(a, sympy.sympify(args.at))
    if args.x is not None:
        taylor = taylor.subs(x, sympy.sympify(args.x))

    print(taylor)


if __name__ == "__main__":
    main()
