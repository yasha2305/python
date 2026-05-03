import json
import os

FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

# Save tasks to file
def save_tasks(tasks):
    try:
        with open(FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print("Error saving tasks:", e)

# Add new task
def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added!")
    else:
        print("Task cannot be empty.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. {task['title']} [{status}]")

# Mark task as done
def mark_done(tasks):
    if not tasks:
        print("No tasks to update.")
        return

    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete task
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()

    try:
        while True:
            print("\n--- TO-DO MENU ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Done")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Choose option: ").strip()

            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                mark_done(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                save_tasks(tasks)
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-5.")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Saving tasks...")
        save_tasks(tasks)

if __name__ == "__main__":
    main()