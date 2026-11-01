"""A simple terminal to-do list app. Tasks are saved in tasks.json."""

import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Read tasks from the file. Return an empty list if there's no file yet."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE) as file:
        return json.load(file)


def save_tasks(tasks):
    """Write all tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks, title):
    """Add a new task that is not done yet."""
    tasks.append({"title": title, "done": False})


def show_tasks(tasks):
    """Print every task with its number and a checkbox."""
    if not tasks:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        checkbox = "[x]" if task["done"] else "[ ]"
        print(f"{number}. {checkbox} {task['title']}")


def mark_done(tasks, number):
    """Mark a task as done. `number` starts at 1, like on screen."""
    tasks[number - 1]["done"] = True


def delete_task(tasks, number):
    """Remove a task and return it. `number` starts at 1, like on screen."""
    return tasks.pop(number - 1)


def ask_task_number(tasks):
    """Ask for a task number. Return it, or None if the input isn't valid."""
    if not tasks:
        print("No tasks yet.")
        return None
    show_tasks(tasks)
    answer = input("Task number: ")
    try:
        number = int(answer)
    except ValueError:
        print("Please type a number.")
        return None
    if number < 1 or number > len(tasks):
        print(f"Please choose a number from 1 to {len(tasks)}.")
        return None
    return number


def main():
    tasks = load_tasks()

    while True:
        print()
        print("=== To-Do List ===")
        print("1. Add a task")
        print("2. Show tasks")
        print("3. Mark a task done")
        print("4. Delete a task")
        print("5. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            if title:
                add_task(tasks, title)
                save_tasks(tasks)
                print(f"Added: {title}")
            else:
                print("The title can't be empty.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            number = ask_task_number(tasks)
            if number is not None:
                mark_done(tasks, number)
                save_tasks(tasks)
                print("Marked as done.")
        elif choice == "4":
            number = ask_task_number(tasks)
            if number is not None:
                removed = delete_task(tasks, number)
                save_tasks(tasks)
                print(f"Deleted: {removed['title']}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, 4 or 5.")


# Only run the app when this file is run directly (not when tests import it).
if __name__ == "__main__":
    main()
