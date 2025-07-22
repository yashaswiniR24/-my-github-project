"""Writing add task"""
def add_todo(): 

    item = input("Enter a to-do item: ").strip() 

    if item: 

        save_todo(item) 

        print("To-do item added.\n") 

    else: 

        print("To-do item cannot be empty.\n") 
