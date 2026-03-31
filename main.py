from logger_config import setup_logger
from storage import load_tasks, save_tasks, load_expenses, save_expenses

logger = setup_logger()




def task_manage():
    print("1.Add Task")
    print("2.Delete Task") 
    print("3.View Task")

    num = input("Enter what you want to do: ")
    logger.info(f"User selected option: {num}")

    tasks = load_tasks()

    # ✅ ADD TASK
    if num == "1":
        task_name = input("Enter task name: ")
        task_complete = input("Is task completed (yes/no): ")
        task_priority = input("Enter priority: ")
        task_due_date = input("Enter due date: ")

        if tasks:
            new_id = tasks[-1]["id"] + 1
        else:
            new_id = 1

        task = {
            "id": new_id,
            "name": task_name,
            "completed": task_complete.lower() == "yes",
            "priority": task_priority,
            "due_date": task_due_date
        }

        tasks.append(task)
        save_tasks(tasks)

        logger.info(f"Task added: {task}")
        print("✅ Task added!")

    # ✅ DELETE TASK
    elif num == "2":
        try:
            task_id = int(input("Enter task ID to delete: "))
            logger.info(f"Deleting task ID: {task_id}")

            new_tasks = [t for t in tasks if t["id"] != task_id]

            save_tasks(new_tasks)

            logger.info(f"Task {task_id} deleted")
            print("✅ Task deleted!")

        except Exception as e:
            logger.error("Delete failed", exc_info=True)

    # ✅ VIEW TASK
    elif num == "3":
        logger.info("Viewing tasks")

        if not tasks:
            print("No tasks found")
        else:
            for t in tasks:
                print(t)

    else:
        logger.warning("Invalid option selected")




def expense_manage():
    categories={"1": "food","2": "travel", "3":"groceries"}
    print("1.food")
    print("2.travel")
    print("3.groceries")

    category=input("Enter the category of expense")
    logger.info(f"User selected category {category}")

    if category not in categories:
        print("❌ Invalid category")
        logger.warning("Invalid expense category selected")
        return
    
    selected_category = categories[category]

    try:
        amount = float(input("Enter amount: "))
    except:
        print("❌ Invalid amount")
        logger.error("Invalid amount entered", exc_info=True)
        return

    date = input("Enter date (YYYY-MM-DD): ")

    # Load existing expenses
    expenses = load_expenses()

    # Create expense object
    expense = {
        "category": selected_category,
        "amount": amount,
        "date": date
    }

    # Add and save
    expenses.append(expense)
    save_expenses(expenses)

    logger.info(f"Expense added: {expense}")
    print("✅ Expense added successfully!")




def main():
    while True:
        print("\n1. Manage Tasks")
        print("2. Manage Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_manage()
        elif choice == "2":
            expense_manage()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


