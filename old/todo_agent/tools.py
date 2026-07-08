tasks = []

def add_task(task: str):
    tasks.append(task)
    return "Task added."

def remove_task(task: str):
    tasks.remove(task)
    return "Task removed."

def list_tasks():
    return "\n".join(tasks)