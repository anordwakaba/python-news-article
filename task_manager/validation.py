from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str):
        return False, "Title must be a string."
    title = title.strip()
    if not title:
        return False, "Title cannot be empty."
    if len(title) > 100:
        return False, "Title too long (max 100 chars)."
    return True, title
    
def validate_task_description(description):
    if description is None:
        return True, ""
    if not isinstance(description, str):
        return False, "Description must be a string."
    description = description.strip()
    if len(description) > 500:
        return False, "Description too long (max 500 chars)."
    return True, description    
    
def validate_due_date(due_date):
    if not isinstance(due_date, str):
        return False, "Due date must be a string in YYYY-MM-DD."
    try:
        dt = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
        return True, dt.isoformat()
    except Exception:
        return False, "Invalid date format. Use YYYY-MM-DD."