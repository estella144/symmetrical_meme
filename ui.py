# This file is part of TaskFlow
# A task management application in Python
# v0.3 (3 Sep 2023, main/79fddc2)

# Summary:
# A Python CLI task management application
# with CRUD operations for tasks, data storage, and error handling.

import logging
import crud as crud
import os

# Logging setup

log_file_path = os.path.join(os.getcwd(), 'filename.log')

logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info(f"Logging set up successfully")

def display_menu():
    logging.info(f"Menu is being displayed")
    print("\nWelcome to TaskFlow")
    print("Warning! This is a development release and may contain bugs.")
    print("Please report bugs to the GitHub repository.")
    print("================================")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Search Tasks")
    print("6. Quit")
    logging.info(f"Menu displayed successfully")

# Define a function to interact with the user and execute actions
def main_menu():
    while True:
        display_menu()

        choice = input("Enter your choice (1/2/3/4/5/6): ")
        logging.debug(f"User selected option {choice} from the menu.")

        if choice == "1":
            logging.info(f"Task is being created")
            title = input("Enter task title: ")
            logging.debug(f"Task title: {title}")
            description = input("Enter task description: ")
            logging.debug(f"Task description: {description}")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            logging.debug(f"Task due date: {due_date}")
            priority = input("Enter priority (1/2/3): ")
            logging.debug(f"Task priority: {priority}")
            logging.debug(f"ui.main_menu() is preparing to run crud.add_task()")
            crud.add_task(title, description, due_date, priority)
            logging.debug(f"Execution returned to ui.main_menu()")
            logging.info(f"Task was created successfully")
        elif choice == "2":
            logging.info(f"Task listing in progress")
            logging.debug(f"ui.main_menu() is preparing to run crud.list_tasks()")
            crud.list_tasks(sort_by_due_date=False, sort_by_priority=False, show_reminders=True)
            logging.info(f"Task listing completed successfully")
        elif choice == "3":
            logging.info("Task is being updated")
            task_index = int(input("Enter the task index to update: "))
            logging.debug(f"Task index chosen: {task_index}")
            new_title = input("Enter the new task title: ")
            logging.debug(f"New task title chosen: {new_title}")
            new_description = input("Enter the new task description: ")
            logging.debug(f"New task description chosen: {new_description}")
            new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
            logging.debug(f"New due date chosen: {new_due_date}")
            new_priority = input("Enter the new priority (1-3):")
            logging.debug(f"New priority chosen: {new_priority}")
            logging.debug(f"ui.main_menu() is preparing to run crud.update_task()")
            crud.update_task(task_index, new_title, new_description, new_due_date, new_priority)
            logging.debug(f"Execution returned to ui.main_menu()")
            logging.info(f"Task was updated successfully")
        elif choice == "4":
            logging.info(f"Task is being deleted")
            task_index = int(input("Enter the task index to delete: "))
            logging.info(f"Task index to delete: {task_index}")
            logging.debug(f"ui.main_menu() is preparing to run crud.delete_task()")
            crud.delete_task(task_index)
            logging.debug(f"Execution returned to ui.main_menu()")
            logging.info(f"Task was deleted successfully")
        elif choice == "5":
            logging.info(f"Task search in progress")
            keyword = input("Enter a keyword to search for: ")
            logging.info(f"Keyword: {keyword}")
            logging.debug(f"ui.main_menu() is preparing to run crud.search_tasks())")
            crud.search_tasks(keyword)
            logging.debug(f"Execution returned to ui.main_menu()")
            logging.info(f"Search successful")
        elif choice == "6":
            logging.info(f"Quitting in progress")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
    logging.info(f"Program terminated normally")
