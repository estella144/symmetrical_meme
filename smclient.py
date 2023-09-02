# Symmetrical Meme
# Task Management Application in Python
# v0.1.dev1 (2 Sep 2023, main/f7fe6e0)

# Summary:
# A Python CLI task management application
# with CRUD operations for tasks, data storage, and error handling.

import os
import csv
import sys

DATA_FILE = "data/tasks.csv"

def add_task(title, description, due_date):
    """Function to add a task."""
    try:
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, description, due_date])
        print("Task added successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to list tasks
def list_tasks(sort_by_due_date=False):
    """Function to list tasks, with optional sorting."""
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            tasks = list(reader)

        if sort_by_due_date:
            tasks.sort(key=lambda x: x[2])  # Sort by due date

        if tasks:
            print("Task List:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. Title: {task[0]}, Description: {task[1]}, Due Date: {task[2]}")
        else:
            print("No tasks found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Tests
# add_task("Task 1", "Description for Task 1", "2023-09-10")
# list_tasks(sort_by_due_date=True)

def update_task(task_index, new_title, new_description, new_due_date):
    """Function to update a task."""
    try:
        with open(DATA_FILE, mode='r') as file:
            tasks = list(csv.reader(file))

        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1] = [new_title, new_description, new_due_date]

            with open(DATA_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task index. Task not updated.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def delete_task(task_index):
    """Function to delete a task."""
    try:
        with open(DATA_FILE, mode='r') as file:
            tasks = list(csv.reader(file))

        if 1 <= task_index <= len(tasks):
            deleted_task = tasks.pop(task_index - 1)

            with open(DATA_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(tasks)
            print(f"Task '{deleted_task[0]}' deleted successfully!")
        else:
            print("Invalid task index. Task not deleted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Tests
# update_task(1, "Updated Task 1", "Updated description", "2023-09-15")
# delete_task(2)

# Function to search tasks by keyword
def search_tasks(keyword):
    """Search tasks by keyword."""
    try:
        with open(DATA_FILE, mode='r') as file:
            tasks = list(csv.reader(file))

        matching_tasks = [task for task in tasks if keyword in task[0] or keyword in task[1]]

        if matching_tasks:
            print(f"Matching tasks for '{keyword}':")
            for index, task in enumerate(matching_tasks):
                print(f"{index + 1}. Title: {task[0]}, Description: {task[1]}, Due Date: {task[2]}")
        else:
            print(f"No tasks found matching '{keyword}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to save tasks to CSV file
def save_tasks_to_file(tasks):
    """Save tasks to CSV file."""
    try:
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print("Tasks saved successfully!")
    except Exception as e:
        print(f"An error occurred while saving tasks: {str(e)}")

# Function to load tasks from CSV file
def load_tasks_from_file():
    """Load tasks from CSV file."""
    try:
        with open(DATA_FILE, mode='r') as file:
            tasks = list(csv.reader(file))
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
