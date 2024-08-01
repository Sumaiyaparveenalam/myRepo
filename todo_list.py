import pickle
import os

# File to store the tasks
TASKS_FILE = 'tasks.pkl'

def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'rb') as file:
            return pickle.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, 'wb') as file:
        pickle.dump(tasks, file)

def add_task(tasks, task):
    """Add a new task."""
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def remove_task(tasks, task):
    """Remove a task."""
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print("Task removed!")
    else:
        print("Task not found!")

def list_tasks(tasks):
    """List all tasks."""
    if tasks:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(tasks, task)
        elif choice == '3':
            list_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
