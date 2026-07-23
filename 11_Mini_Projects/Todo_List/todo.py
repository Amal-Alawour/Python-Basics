tasks = []

while True:
    print("\n=== Todo List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_number = int(input("Enter the task number to remove: "))
                removed_task = tasks.pop(task_number - 1)
                print(f'"{removed_task}" removed successfully!')
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
