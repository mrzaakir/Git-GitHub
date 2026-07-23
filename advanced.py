"""A small task planner project."""

def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet("world"))

tasks = []


def add_task(title: str) -> None:
    tasks.append(title)

def list_tasks() -> None:
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def save_tasks(path: str = "tasks.txt") -> None:
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(tasks))

def load_tasks(path: str = "tasks.txt") -> None:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return [line.strip() for line in handle if line.strip()]
    except FileNotFoundError:
        return []

tasks = load_tasks()

def read_input(prompt: str) -> str:
    return input(prompt).strip()

def main() -> None:
    print("Task planner ready")
    while True:
        choice = read_input("Choose action (add/list/quit): ").lower()
        if choice == "quit":
            break
        if choice == "add":
            title = read_input("Task title: ")
            add_task(title)
        elif choice == "list":
            list_tasks()

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple task planner")
    parser.add_argument("command", nargs="?", default="list")
    parser.add_argument("title", nargs="?", default="")
    return parser

def run_from_cli() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "add" and args.title:
        add_task(args.title)
    elif args.command == "list":
        list_tasks()

from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool = False

def add_task_object(task: Task) -> None:
    tasks.append(task)

def list_task_objects() -> None:
    for index, task in enumerate(tasks, start=1):
        marker = "x" if task.done else " "
        print(f"{index}. [{marker}] {task.title}")

def complete_task(index: int) -> None:
    if 0 <= index < len(tasks):
        tasks[index].done = True

def remove_task(index: int) -> None:
    if 0 <= index < len(tasks):
        tasks.pop(index)

def active_tasks() -> list[Task]:
    return [task for task in tasks if not task.done]

class TaskError(Exception):
    """Raised when a task operation is invalid."""

def ensure_title(title: str) -> str:
    if not title.strip():
        raise TaskError("Task title cannot be empty")
    return title.strip()

from typing import Iterable


def summarize(tasks: Iterable[Task]) -> str:
    return " | ".join(task.title for task in tasks)

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("task_planner")

def log_action(action: str, task: Task) -> None:
    logger.info("%s -> %s", action, task.title)

from functools import wraps


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Calling %s", func.__name__)
        return func(*args, **kwargs)
    return wrapper
