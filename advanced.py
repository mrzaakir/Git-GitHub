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
        task = tasks[index]
        log_action("removed", task)
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

@log_calls
def display_tasks() -> None:
    list_task_objects()

from contextlib import contextmanager


@contextmanager
def task_file(path: str):
    handle = open(path, "a", encoding="utf-8")
    try:
        yield handle
    finally:
        handle.close()

def append_task_to_file(path: str, task: Task) -> None:
    with task_file(path) as handle:
        handle.write(task.title + "\n")

def yield_titles(tasks: Iterable[Task]):
    for task in tasks:
        yield task.title

from pathlib import Path


def data_path(name: str = "tasks.json") -> Path:
    return Path(__file__).with_name(name)

import json


def save_to_json(path: str | None = None) -> None:
    destination = Path(path or data_path())
    payload = [{"title": task.title, "done": task.done} for task in tasks]
    destination.write_text(json.dumps(payload, indent=2), encoding="utf-8")

def load_from_json(path: str | None = None) -> None:
    destination = Path(path or data_path())
    if destination.exists():
        payload = json.loads(destination.read_text(encoding="utf-8"))
        global tasks
        tasks = [Task(title=item["title"], done=item.get("done", False)) for item in payload]

def main_cli() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "add" and args.title:
        task = Task(title=ensure_title(args.title))
        add_task_object(task)
        save_to_json()
    elif args.command == "list":
        display_tasks()

if __name__ == "__main__":
    main_cli()
