# This file is part of Symmetrical Meme
# A task management application in Python
# v0.2.dev4 (2 Sep 2023, main/bfdf685)

# Summary:
# A Python CLI task management application
# with CRUD operations for tasks, data storage, and error handling.

import tkinter as tk
from tkinter import messagebox
import smcrud as crud

# Function to add a task (you'll need to implement this)
def add_task_gui():
    # Create a new tkinter window for adding tasks
    add_window = tk.Toplevel()
    add_window.title("Add Task")

    # Create labels and entry fields for task details
    title_label = tk.Label(add_window, text="Title:")
    title_entry = tk.Entry(add_window)

    description_label = tk.Label(add_window, text="Description:")
    description_entry = tk.Entry(add_window)

    due_date_label = tk.Label(add_window, text="Due Date:")
    due_date_entry = tk.Entry(add_window)

    priority_label = tk.Label(add_window, text="Priority:")
    priority_entry = tk.Entry(add_window)

    # Function to save the task
    def save_task():
        # Get user input from the entry fields
        title = title_entry.get()
        description = description_entry.get()
        due_date = due_date_entry.get()
        priority = priority_entry.get()  # Get priority input

        # Call the core function to add the task
        crud.add_task(title, description, due_date, priority)  # Pass priority to add_task

        # Close the add window
        add_window.destroy()

    # Create a button to save the task
    save_button = tk.Button(add_window, text="Save Task", command=save_task)

    # Pack the elements onto the window
    title_label.pack()
    title_entry.pack()

    description_label.pack()
    description_entry.pack()

    due_date_label.pack()
    due_date_entry.pack()

    priority_label.pack()
    priority_entry.pack()

    save_button.pack()

# Function to list tasks (you'll need to implement this)
def list_tasks_gui():
    # Function to list tasks
def list_tasks_gui():
    # Create a new tkinter window for listing tasks
    list_window = tk.Toplevel()
    list_window.title("List Tasks")

    # Call the core function to list tasks
    tasks = list_tasks()

    # Create a text widget to display tasks
    task_text = tk.Text(list_window)
    task_text.pack()

    # Display tasks in the text widget
    for task in tasks:
        task_text.insert(tk.END, f"Title: {task['title']}\n")
        task_text.insert(tk.END, f"Description: {task['description']}\n")
        task_text.insert(tk.END, f"Due Date: {task['due_date']}\n")
        task_text.insert(tk.END, f"Priority: {task['priority']}\n\n")

    # Make the text widget read-only
    task_text.config(state=tk.DISABLED)
