def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. Show menu")
    print("2. Add task")
    print("3. remove task")
    print("4. exit")


def main():
    tasks = []
    while True:
        show_menu()
        pick = input("Choose 1-4:""")

        if pick == "1":
            show_tasks(tasks)
        elif pick == "2":
            add_task(tasks)
        elif pick == "3":
            remove_task(tasks)
        elif pick == "4":
            print("Exit")
            break
        else:
            print("Try again")


def show_tasks(tasks):
    if not tasks:
        print("List is empty")
    else:
        for task in tasks:
            print(task)


def add_task(tasks):
    task = input("Enter new task:")
    tasks.append(task)
    print(f"'{task}'added.")


def remove_task(tasks):
    show_tasks(tasks)
    task_number = int(input("Choose number:"))
    remove_task = tasks.pop(task_number - 1)
    print(f"'{remove_task}' is removed.")


if __name__ == "__main__":
    main()
