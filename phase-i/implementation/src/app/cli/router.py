import sys
from src.app.services.todo_service import TodoService

class CliRouter:
    def __init__(self):
        self._service = TodoService()

    def display_menu(self):
        print("\n--- Todo App Menu ---")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

    def run(self):
        print("Welcome to Todo App")
        while True:
            self.display_menu()
            choice = input("\nSelect an option (1-6): ").strip()

            if choice == "1":
                self._handle_create()
            elif choice == "2":
                self._handle_view()
            elif choice == "3":
                self._handle_update()
            elif choice == "4":
                self._handle_done()
            elif choice == "5":
                self._handle_delete()
            elif choice == "6":
                print("\nExiting... Goodbye!")
                sys.exit(0)
            else:
                print("\n[!] Invalid selection. Please enter a number between 1 and 6.")

    def _handle_create(self):
        desc = input("\nEnter task description: ").strip()
        try:
            task = self._service.add_task(desc)
            print(f"\n[+] Task '{task.description}' created with ID: {task.id}")
        except ValueError as e:
            print(f"\n[!] Error: {e}")

    def _handle_view(self):
        tasks = self._service.get_all_tasks()
        if not tasks:
            print("\nYour Todo list is empty.")
            return

        print("\n--- Your Tasks ---")
        for task in tasks:
            print(task)

    def _handle_update(self):
        try:
            task_id = int(input("\nEnter task ID to update: "))
            new_desc = input("Enter new description: ").strip()
            task = self._service.update_task(task_id, new_desc)
            if task:
                print(f"\n[+] Task {task_id} updated successfully.")
            else:
                print(f"\n[!] Task with ID {task_id} not found.")
        except ValueError:
            print("\n[!] Error: Please enter a valid numeric ID.")

    def _handle_done(self):
        try:
            task_id = int(input("\nEnter task ID to mark as done: "))
            task = self._service.mark_task_done(task_id)
            if task:
                print(f"\n[+] Task {task_id} marked as done.")
            else:
                print(f"\n[!] Task with ID {task_id} not found.")
        except ValueError:
            print("\n[!] Error: Please enter a valid numeric ID.")

    def _handle_delete(self):
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            if self._service.delete_task(task_id):
                print(f"\n[+] Task {task_id} deleted successfully.")
            else:
                print(f"\n[!] Task with ID {task_id} not found.")
        except ValueError:
            print("\n[!] Error: Please enter a valid numeric ID.")
