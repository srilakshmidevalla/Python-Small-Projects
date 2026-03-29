# project_02_todo_list.py
# Mini Project 2: Command-Line To-Do List (with file persistence)
# Run: python 06_mini_projects/project_02_todo_list.py

import json
import os

TODO_FILE = "06_mini_projects/todos.json"

# ---- DATA LAYER ----
def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

# ---- ACTIONS ----
def add_todo(todos, task):
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"✅ Added: '{task}'")

def list_todos(todos):
    if not todos:
        print("📭 No tasks yet!")
        return
    print("\n📋 YOUR TO-DO LIST")
    print("-" * 30)
    for i, item in enumerate(todos, start=1):
        status = "✓" if item["done"] else "○"
        print(f"  {i}. [{status}] {item['task']}")
    print("-" * 30)
    done_count = sum(1 for t in todos if t["done"])
    print(f"  {done_count}/{len(todos)} completed\n")

def complete_todo(todos, index):
    if 1 <= index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        print(f"🎉 Completed: '{todos[index - 1]['task']}'")
    else:
        print("Invalid task number.")

def delete_todo(todos, index):
    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        save_todos(todos)
        print(f"🗑️  Deleted: '{removed['task']}'")
    else:
        print("Invalid task number.")

def clear_done(todos):
    before = len(todos)
    todos[:] = [t for t in todos if not t["done"]]
    save_todos(todos)
    print(f"🧹 Cleared {before - len(todos)} completed task(s).")

# ---- MENU ----
def show_menu():
    print("\n--- MENU ---")
    print("  a → Add task")
    print("  l → List tasks")
    print("  c → Complete task")
    print("  d → Delete task")
    print("  x → Clear completed")
    print("  q → Quit")

def main():
    print("=" * 35)
    print("   📝 PYTHON TO-DO LIST")
    print("=" * 35)
    todos = load_todos()

    while True:
        show_menu()
        choice = input("\nAction: ").strip().lower()

        if choice == "a":
            task = input("New task: ").strip()
            if task:
                add_todo(todos, task)
        elif choice == "l":
            list_todos(todos)
        elif choice == "c":
            list_todos(todos)
            try:
                num = int(input("Complete task #: "))
                complete_todo(todos, num)
            except ValueError:
                print("Enter a number.")
        elif choice == "d":
            list_todos(todos)
            try:
                num = int(input("Delete task #: "))
                delete_todo(todos, num)
            except ValueError:
                print("Enter a number.")
        elif choice == "x":
            clear_done(todos)
        elif choice == "q":
            print("👋 Goodbye!")
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
