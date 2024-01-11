---

# Lockboxes Problem

This repository provides a solution to the Lockboxes Problem, a common algorithmic challenge involving unlocking boxes within a set of nested boxes. The problem is solved using Python, and the `canUnlockAll` function is implemented to determine whether all boxes can be successfully opened.

## Problem Statement

You have `n` number of locked boxes in front of you, each numbered sequentially from 0 to `n - 1`. Each box may contain keys to other boxes, and a key with the same number as a box can open that box. The goal is to determine if it is possible to open all the boxes starting from the first box, which is already unlocked.

## Implementation

The solution is implemented in Python and can be found in the `0-lockboxes.py` file. The `canUnlockAll` function takes a list of boxes as input, where each box is represented as a list of keys. The function returns `True` if all boxes can be opened and `False` otherwise.

## Usage

To test the solution, you can use the provided `main.py` script. The script includes test cases with different sets of boxes, demonstrating the functionality of the `canUnlockAll` function.

```bash
$ ./main_0.py
```

Feel free to explore and modify the code to adapt it to your specific use cases.

## Contributions

Contributions to this repository are welcome! If you have improvements, additional test cases, or other enhancements, feel free to open a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).

---
