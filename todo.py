import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    tasks = load_tasks()
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
