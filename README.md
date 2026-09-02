 # Task Manager Lab

Simple task management system implemented in Python.

Project structure:
- `main.py` — interactive CLI
- `task_manager/validation.py` — input validation functions
- `task_manager/task_utils.py` — task operations (add, mark complete, view, progress)
- `test_runner.py` — non-interactive smoke test

Usage (WSL):

```bash
# open in VS Code
code ~/task_manager_lab

# run interactive CLI
python3 ~/task_manager_lab/main.py

# run smoke test
python3 ~/task_manager_lab/test_runner.py
```

No external dependencies required.