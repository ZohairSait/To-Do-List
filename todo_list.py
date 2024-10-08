# Simple To-Do List Program

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Mark a Task as Complete")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- Your To-Do List ---")
    for idx, (task, status) in enumerate(tasks, start=1):
        status_str = "Complete" if status else "Incomplete"
        print(f"{idx}. {task} [{status_str}]")

def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append((task, False))
    print(f"Task '{task}' added to the list.")

def remove_task(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)[0]
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_complete(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num] = (tasks[task_num][0], True)
            print(f"Task '{tasks[task_num][0]}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_complete(tasks)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
