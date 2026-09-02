from datetime import datetime

# Import validation functions
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    ok, res = validate_task_title(title)
    if not ok:
        print(f"Title error: {res}")
        return False
    ok, res = validate_task_description(description)
    if not ok:
        print(f"Description error: {res}")
        return False
    ok, res = validate_due_date(due_date)
    if not ok:
        print(f"Due date error: {res}")
        return False

    task = {
        "title": title.strip(),
        "description": description.strip() if description is not None else "",
        "due_date": res,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    return True

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not isinstance(index, int):
        print("Index must be an integer.")
        return False
    if index < 1 or index > len(tasks):
        print("Invalid task index.")
        return False
    tasks[index - 1]["completed"] = True
    print("Task marked as complete!")
    return True

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [(i + 1, t) for i, t in enumerate(tasks) if not t.get("completed", False)]
    if not pending:
        print("No pending tasks.")
        return []
    for idx, task in pending:
        print(f"{idx}. {task['title']} - Due: {task['due_date']}")
        if task.get('description'):
            print(f"   {task['description']}")
    return pending

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        progress = 0.0
    else:
        completed = sum(1 for t in tasks if t.get("completed", False))
        progress = (completed / total) * 100
    return round(progress, 2)