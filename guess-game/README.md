# Guess Game

A number guessing game for the terminal. The computer picks a secret number from 1 to 100, and you keep guessing, with "too high" or "too low" hints, until you get it.

## Run

Python 3, standard library only.

```bash
python3 guess.py
```

## How it works

- Invalid input (text, or a number outside 1 to 100) is rejected and not counted as an attempt
- When you win, it tells you how many attempts you took
- The range is set by `LOWEST` and `HIGHEST` at the top of `guess.py`

## Files

- `guess.py`: the game
