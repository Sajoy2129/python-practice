# To-Do List

A simple terminal to-do list app written in Python. Add tasks, mark them done, and delete
them. Everything is saved automatically, so your list is still there next time.

Uses only the Python standard library, so there's nothing to install.

## Features

- **Add a task**
- **Show all tasks** with a checkbox: `[ ]` for not done, `[x]` for done
- **Mark a task as done**
- **Delete a task**
- Tasks are saved to `tasks.json` after every change

## Requirements

- Python 3

## Getting started

```bash
git clone https://github.com/Sajoy2129/todo-list.git
cd todo-list
python3 todo.py
```

## Usage

```
=== To-Do List ===
1. Add a task
2. Show tasks
3. Mark a task done
4. Delete a task
5. Quit
Choose an option: 1
Task title: Buy milk
Added: Buy milk

Choose an option: 2
1. [ ] Buy milk
2. [x] Learn git
```

To mark a task done or delete it, choose option 3 or 4. The app shows your tasks and asks
for the task's number.

## Data file

Tasks are stored in `tasks.json` in the folder you run the app from:

```json
[
  {
    "title": "Buy milk",
    "done": false
  },
  {
    "title": "Learn git",
    "done": true
  }
]
```

`tasks.json` is listed in `.gitignore`, so your personal tasks are never committed.

## Project structure

```
todo.py    # the whole app: task logic, saving/loading, and the terminal menu
```
