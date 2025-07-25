"""Writing delete task"""
def delete_todo():
    todos = load_todos()
    view_todos()
    try:
        index = int(input("Enter the number of the to-do to delete: "))
        if 1 <= index <= len(todos):
            removed = todos.pop(index - 1)
            save_all_todos(todos)
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid index.\n")
    except ValueError:
        print("Please enter a valid number.\n")
