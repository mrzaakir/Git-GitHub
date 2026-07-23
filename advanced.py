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
