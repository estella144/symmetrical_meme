# This file is part of TaskFlow
# A task management application in Python
# v0.2.dev6 (3 Sep 2023, main/f9bc386)

# Summary:
# A Python CLI task management application
# with CRUD operations for tasks, data storage, and error handling.

import os
import csv
import sys
from sys import platform
import logging
from datetime import datetime, timedelta

# Flag to change the default data file
DEV_MODE = True

# Data file setup
# Determine the directory containing the script
script_dir = os.path.dirname(os.path.realpath(__file__))
# Change the working directory to the script directory
os.chdir(script_dir)
if platform == "linux" or platform == "linux2":
    if DEV_MODE:
        DATA_FILE = os.path.join(os.getcwd(), "data/tasks.csv")
    else:
        DATA_FILE = os.path.join(os.getcwd(), "data/tasks.csv")
elif platform == "darwin":
    if DEV_MODE:
        DATA_FILE = os.path.join(os.getcwd(), "data/tasks.csv")
    else:
        DATA_FILE = os.path.join(os.getcwd(), "data/tasks.csv")
elif platform == "win32":
    if DEV_MODE:
        DATA_FILE = os.path.join(os.getcwd(), "data\\tasks.csv")
    else:
        DATA_FILE = os.path.join(os.getcwd(), "data\\tasks.csv")

print(DATA_FILE)

# ANSI color codes for colour-coding of tasks

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'  # Reset color to default

# Logging setup
log_file_path = os.path.join(os.getcwd(), 'filename.log')

logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def add_task(title, description, due_date, priority):
    """Function to add a task."""
    logging.info("Adding task, attempting to open file")
    try:
        with open(DATA_FILE, mode='a', newline='') as file:
            logging.debug("Writing task to file")
            writer = csv.writer(file)
            writer.writerow([title, description, due_date, priority])
            logging.debug("File written to successfully")
        print("Task added successfully!")
        logging.info("Task added successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"An error occured while adding task: {str(e)}")

def print_task_list(tasks, show_reminders):
    """Function to print task list."""
    logging.info("Tasks found, listing tasks")
    print("Task List:")
    today = datetime.today().date()
    reminder_threshold = today + timedelta(days=1)

    for index, task in enumerate(tasks):
        due_date = datetime.strptime(task[2], '%Y-%m-%d').date()
        if due_date < today:
            print(f"{index + 1}. Title: {RED}{task[0]}{RESET}, Description: {task[1]}, Due Date: {task[2]}, Priority: {task[3]}")
            if show_reminders:
                print(f"{RED}   Reminder: Task '{task[0]}' is overdue!{RESET}")
        elif due_date == today:
            print(f"{index + 1}. Title: {YELLOW}{task[0]}{RESET}, Description: {task[1]}, Due Date: {task[2]}, Priority: {task[3]}")
            if show_reminders:
                print(f"{YELLOW}   Reminder: Task '{task[0]}' is due today!{RESET}")
        else:
            print(f"{index + 1}. Title: {GREEN}{task[0]}{RESET}, Description: {task[1]}, Due Date: {task[2]}, Priority: {task[3]}")
            if show_reminders and today <= due_date <= reminder_threshold:
                print(f"{YELLOW}   Reminder: Task '{task[0]}' is due soon!{RESET}")

def list_tasks(sort_by_due_date=False, sort_by_priority=False, show_reminders=True):
    """Function to list tasks, with optional sorting."""
    logging.info("Adding task, attempting to open file")
    try:
        with open(DATA_FILE, mode='r') as file:
            logging.debug("Reading tasks from file")
            reader = csv.reader(file)
            tasks = list(reader)
            logging.debug("File read successfully")

        if sort_by_due_date:
            tasks.sort(key=lambda x: datetime.strptime(x[2], '%Y-%m-%d'))  # Sort by due date
            logging.debug("Tasks sorted by due date")
        elif sort_by_priority:
            tasks.sort(key=lambda x: x[3], reverse=True) # Sort by priority
            logging.debug("Tasks sorted by priority")

        if tasks:
            print_task_list(tasks, show_reminders)
            logging.info("Tasks listed successfully")
            return tasks
        else:
            logging.info("No tasks found, success")
            print("No tasks found.")
            return tasks
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"An error occurred: {str(e)}")

# Tests
# add_task("Task 1", "Description for Task 1", "2023-09-10")
# list_tasks(sort_by_due_date=True)

def update_task(task_index, new_title, new_description, new_due_date, new_priority):
    """Function to update a task."""
    logging.info("Updating task, attempting to open file")
    try:
        with open(DATA_FILE, mode='r') as file:
            tasks = list(csv.reader(file))
        logging.debug("File opened successfully")

        if 1 <= task_index <= len(tasks):
            logging.info("Task")
            tasks[task_index - 1] = [new_title, new_description, new_due_date, new_priority]

            with open(DATA_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(tasks)
            print("Task updated successfully!")
            logging.info("Task updated successfully!")
        else:
            print("Invalid task index. Task not updated.")
            logging.warning("Invalid task index. Task not updated.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"An error occurred: {str(e)}")

def delete_task(task_index):
    """Function to delete a task."""
    logging.info("Deleting task, attempting to open file")
    try:
        with open(DATA_FILE, mode='r') as file:
            tasks = list(csv.reader(file))
        logging.debug("File opened successfully")

        if 1 <= task_index <= len(tasks):
            deleted_task = tasks.pop(task_index - 1)

            with open(DATA_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(tasks)
            print(f"Task '{deleted_task[0]}' deleted successfully!")
            logging.info(f"Task '{deleted_task[0]}' deleted successfully!")
        else:
            print("Invalid task index. Task not deleted.")
            logging.warning("Invalid task index. Task not deleted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"An error occurred: {str(e)}")

# Tests
# update_task(1, "Updated Task 1", "Updated description", "2023-09-15")
# delete_task(2)

# Function to search tasks by keyword
def search_tasks(keyword):
    """Search tasks by keyword."""
    logging.info("Searching tasks by keyword, attempting to open file")
    try:
        with open(DATA_FILE, mode='r') as file:
            tasks = list(csv.reader(file))
        logging.debug("File opened successfully")

        matching_tasks = [task for task in tasks if keyword in task[0] or keyword in task[1]]

        if matching_tasks:
            logging.info("Found matching tasks successfully")
            print(f"Matching tasks for '{keyword}':")
            for index, task in enumerate(matching_tasks):
                print(f"{index + 1}. Title: {task[0]}, Description: {task[1]}, Due Date: {task[2]}")
        else:
            logging.info("No matching tasks found, success")
            print(f"No tasks found matching '{keyword}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"An error occurred: {str(e)}")

# Function to save tasks to CSV file
def save_tasks_to_file(tasks):
    """Save tasks to CSV file."""
    logging.info("Saving tasks to CSV file")
    try:
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print("Tasks saved successfully!")
        logging.info("Tasks saved successfully!")
    except Exception as e:
        print(f"An error occurred while saving tasks: {str(e)}")
        logging.error(f"An error occurred while saving tasks: {str(e)}")

# Function to load tasks from CSV file
def load_tasks_from_file():
    """Load tasks from CSV file."""
    logging.info("Loading tasks from CSV file")
    try:
        with open(DATA_FILE, mode='r') as file:
            tasks = list(csv.reader(file))
        logging.info("Tasks loaded from CSV file successfully")
        return tasks
    except Exception as e:
        print(f"An error occurred while loading tasks: {str(e)}")
        return []

# More tests
# search_tasks("Updated")
# tasks = load_tasks_from_file()
# print("Loaded tasks:")
# for index, task in enumerate(tasks):
#     print(f"{index + 1}. Title: {task[0]}, Description: {task[1]}, Due Date: {task[2]}")

def user_feedback(message, success=True):
    """Sends feedback to the user."""
    if success:
        print(f"Success: {message}")
    else:
        print(f"Error: {message}")

# Function to handle invalid user input
def handle_invalid_input():
    """Handles invalid user input."""
    print("Invalid input. Please try again.")

# More tests, oh yes!
# user_feedback("Task added successfully!")
# handle_invalid_input()

if __name__ == "__main__":
    print("This file is not intended to be run directly!")
    print("To run TaskFlow, run ui.py.")
