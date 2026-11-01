# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running

Use `python3` (macOS, Python 3.13):

```
python3 calculator.py
```

No dependencies, build step, or test suite yet.

## Structure

`calculator.py` is a menu-driven terminal calculator. There's one function per menu action (`add`, `subtract`, `multiply`, `divide`, `power`, `square_root`, `quit_program`). The math functions only return values, and they return an `"Error: ..."` string for invalid input instead of raising. `main()` does all the printing. `main()` loops: `show_menu()`, read a choice from 1 to 7, read numbers with `get_number()` (which keeps asking until the input is valid), then print the result. Square root (6) reads one number; the others read two. Choosing 7 calls `quit_program()` and exits the loop.

## Working with the user

The user is a Python beginner. Keep code simple and beginner-friendly, and after every change explain what was done in plain terms and point out any new Python concept.
