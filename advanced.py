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
