# CLAUDE.md

This file gives Claude Code context about this project. Claude reads it at the start of every session.

## About me

- I'm a beginner developer, still learning how code works.
- Explain every step in plain language before and after doing it.
- When you write code, explain what each important line or block does and why.
- Define technical terms the first time you use them (e.g. "variable", "loop", "function").
- Prefer simple, readable code over clever or compact code.
- Make small changes one at a time so I can follow along.
- Before running commands that change files or git history, tell me what they will do.

## Project

A number guessing game written in Python that runs in the terminal.
The computer picks a random number, and the player guesses until they get it right,
getting "too high" / "too low" hints along the way.

## How to run

```bash
python3 main.py
```

## Code style

- Python 3, standard library only (no extra packages unless we discuss it first).
- Use clear, descriptive variable names (`secret_number`, not `n`).
- Add short comments explaining *why* something is done, aimed at a beginner reader.
