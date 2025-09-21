# Simple To-Do List

tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")
    elif choice == '2':
        if tasks:
            print("Your Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        else:
            print("No tasks yet.")
    elif choice == '3':
        if tasks:
            print("Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            task_num = int(input("Enter task number to remove: "))
            if 0 < task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed!")
            else:
                print("Invalid number!")
        else:
            print("No tasks to remove.")
    elif choice == '4':
        print("Exiting To-Do List.")
        break
    else:
        print("Invalid choice! Try again.")
