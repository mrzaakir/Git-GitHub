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
