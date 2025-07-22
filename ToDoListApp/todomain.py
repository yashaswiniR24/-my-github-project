from marktask import mark_complete
from deletetask import delete_todo
def load_todos():
    try:
        with open("todos.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_all_todos(todos):
    try:
        with open("todos.txt", "w") as file:
            for item in todos:
                file.write(item + "\n")
    except Exception as e:
        print(f"Error saving to file: {e}")

def save_todo(item):
    try:
        with open("todos.txt", "a") as file:
            file.write(item + "\n")
    except Exception as e:
        print(f"Error saving to file: {e}")

def todo_menu():
    while True:
        print("To-Do List Menu:")
        print("1. Add To-Do")
        print("2. View To-Dos")
        print("3. Delete To-Do")
        print("4. Mark To-Do as Complete")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_todo()
        elif choice == "2":
            view_todos()
        elif choice == "3":
            delete_todo()
        elif choice == "4":
            mark_complete()
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")

todo_menu()