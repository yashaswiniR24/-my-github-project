"""Writing mark task"""

def mark_complete():
    todos = load_todos()
    view_todos()
    try:
        index = int(input("Enter the number of the to-do to mark as complete: "))
        if 1 <= index <= len(todos):
            todos[index - 1] += " [✓]"
            save_all_todos(todos)
            print(f"Marked as complete: {todos[index - 1]}\n")
        else:
            print("Invalid index.\n")
    except ValueError:
        print("Please enter a valid number.\n")