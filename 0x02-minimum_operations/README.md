# MinOperations Task

## Overview

This repository contains the solution for the "MinOperations" task. The problem involves determining the minimum number of operations needed to obtain 'n' 'H' characters in a text file, given two available operations: Copy All and Paste.

## Problem Description

You start with a single character 'H' in a text file. The two available operations are:

1. **Copy All:** Copies all characters in the file.
2. **Paste:** Pastes the characters that were copied.

The goal is to find the minimum number of operations needed to achieve exactly 'n' 'H' characters in the file.

## Implementation

The solution is implemented in Python and consists of a function `minOperations(n)` that takes an integer 'n' as input and returns the minimum number of operations required. The function uses a loop to perform Copy All and Paste operations until the desired 'n' 'H' characters are obtained.

## Usage

To test the solution, use the provided `minOperations` function in your Python script or interactively in a Python environment.

```python
from minoperations import minOperations

# Test cases
n1 = 4
result1 = minOperations(n1)
print(f"Min # of operations to reach {n1} char: {result1}")

n2 = 12
result2 = minOperations(n2)
print(f"Min # of operations to reach {n2} char: {result2}")
```

## Testing

The repository includes a `test_minoperations.py` file with test cases for the solution. Run the tests using a testing framework like `pytest`.

```bash
pytest test_minoperations.py
```

## Contributions

Contributions are welcome! If you have any improvements or suggestions, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
