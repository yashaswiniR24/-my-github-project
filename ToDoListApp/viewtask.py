"""Writing view task"""

def view_todos(): 

    todos = load_todos() 

    if not todos: 

        print("No to-do items found.\n") 

    else: 

        print("\nYour To-Do List:") 

        for idx, item in enumerate(todos, 1): 

            print(f"{idx}. {item}") 

        print() 
