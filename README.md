# Taylor Expander

A Python tool for computing Taylor polynomial approximations of mathematical functions using **SymPy**.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![SymPy](https://img.shields.io/badge/SymPy-Latest-orange)](https://www.sympy.org/)

---

## Installation 📦

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/taylor-expander.git
   cd taylor-expander
   ```

2. **Install dependencies**:
   ```bash
   pip install sympy
   ```

---

## Usage 🚀

### Command-Line Arguments

| Flag | Description | Example |
|------|-------------|---------|
| `-f` | Function to approximate | `"exp(x)"` |
| `-a` | Expansion point | `--at 1` |
| `-x` | Substitute `x` with a value | `--x 0.5` |
| `-d` | Maximum derivative degree (default: 5) | `--derivatives 3` |

### Examples

1. **Basic Taylor series for `e^x` (up to 3rd derivative)**:
   ```bash
   python taylor.py -f "exp(x)" -a 0 -d 3
   ```
   **Output**:
   ```
   1 + x + x**2/2
   ```

2. **Taylor series for `sin(x)` around `a = π/2`**:
   ```bash
   python taylor.py -f "sin(x)" -a "pi/2" -d 5
   ```

3. **Numerical approximation at `x = 1` for `cos(x)`**:
   ```bash
   python taylor.py -f "cos(x)" -x 1
   ```

---

## How It Works 🔧

1. **Symbolic Differentiation**: Uses SymPy to compute derivatives symbolically.
2. **Series Construction**: Builds the polynomial using the formula:
   \[
   T(x) = \sum_{n=0}^{d} \frac{f^{(n)}(a)}{n!}(x-a)^n
   \]

---

## Limitations

- **Non-analytic Functions**: May fail for functions without a Taylor series representation.
- **High-Degree Derivatives**: Computational cost grows with `-d` (use values ≤ 10 for practicality).

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-idea`)
3. Submit a pull request!

---

## License 📄

MIT License - See [LICENSE](LICENSE) for details.
