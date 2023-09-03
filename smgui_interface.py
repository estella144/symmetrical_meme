# This file is part of Symmetrical Meme
# A task management application in Python
# v0.2.dev7 (2 Sep 2023, main/bfdf685)

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

# Function to list tasks
def list_tasks_gui():
    # Create a new tkinter window for listing tasks
    list_window = tk.Toplevel()
    list_window.title("List Tasks")

    # Call the core function to list tasks
    tasks = crud.list_tasks()

    if tasks is None:
        # Handle the case when tasks are not retrieved
        messagebox.showerror("Error", "Failed to retrieve tasks.")
        return

    # Debugging: Print tasks to check if they are retrieved correctly
    print(tasks)

    # Create a text widget to display tasks
    task_text = tk.Text(list_window)
    task_text.pack()

    # Display tasks in the text widget
    for task in tasks:
        task_text.insert(tk.END, f"Title: {task[0]}\n")
        task_text.insert(tk.END, f"Description: {task[1]}\n")
        task_text.insert(tk.END, f"Due Date: {task[2]}\n")
        task_text.insert(tk.END, f"Priority: {task[3]}\n\n")

    # Make the text widget read-only
    task_text.config(state=tk.DISABLED)

# Function to update a task
def update_task_gui():
    # Create a new tkinter window for updating tasks
    update_window = tk.Toplevel()
    update_window.title("Update Task")

    # Create labels and entry fields for task details
    title_label = tk.Label(update_window, text="Title:")
    title_entry = tk.Entry(update_window)

    description_label = tk.Label(update_window, text="Description:")
    description_entry = tk.Entry(update_window)

    due_date_label = tk.Label(update_window, text="Due Date:")
    due_date_entry = tk.Entry(update_window)

    priority_label = tk.Label(update_window, text="Priority:")
    priority_entry = tk.Entry(update_window)

    # Function to save the updated task
    def save_updated_task():
        # Get user input from the entry fields
        title = title_entry.get()
        description = description_entry.get()
        due_date = due_date_entry.get()
        priority = priority_entry.get()

        # Call the core function to update the task
        crud.update_task(task_id, title, description, due_date, priority)

        # Close the update window
        update_window.destroy()

    # Create a button to save the updated task
    save_button = tk.Button(update_window, text="Save Task", command=save_updated_task)

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

# Function to delete a task
def delete_task_gui():
    # Create a new tkinter window for deleting tasks
    delete_window = tk.Toplevel()
    delete_window.title("Delete Task")

    # Create a label and entry field for task ID
    task_id_label = tk.Label(delete_window, text="Task ID:")
    task_id_entry = tk.Entry(delete_window)

    # Function to delete the task
    def delete_selected_task():
        # Get the task ID from the entry field
        task_id = task_id_entry.get()

        # Call the core function to delete the task
        # You'll need to implement the delete_task() function in smcrud.py
        crud.delete_task(task_id)

        # Close the delete window
        delete_window.destroy()

    # Create a button to delete the task
    delete_button = tk.Button(delete_window, text="Delete Task", command=delete_selected_task)

    # Pack the elements onto the window
    task_id_label.pack()
    task_id_entry.pack()
    delete_button.pack()

# Function to search for tasks
def search_tasks_gui():
    # Create a new tkinter window for searching tasks
    search_window = tk.Toplevel()
    search_window.title("Search Tasks")

    # Create a label and entry field for search keywords
    search_label = tk.Label(search_window, text="Search Keywords:")
    search_entry = tk.Entry(search_window)

    # Function to perform the search
    def perform_search():
        # Get search keywords from the entry field
        keywords = search_entry.get()

        # Call the core function to search for tasks
        matching_tasks = crud.search_tasks(keywords)

        # Display matching tasks in a text widget
        matching_text = tk.Text(search_window)
        matching_text.pack()

        for task in matching_tasks:
            matching_text.insert(tk.END, f"Title: {task['title']}\n")
            matching_text.insert(tk.END, f"Description: {task['description']}\n")
            matching_text.insert(tk.END, f"Due Date: {task['due_date']}\n")
            matching_text.insert(tk.END, f"Priority: {task['priority']}\n\n")

        # Make the text widget read-only
        matching_text.config(state=tk.DISABLED)

    # Create a button to perform the search
    search_button = tk.Button(search_window, text="Search", command=perform_search)

    # Pack the elements onto the window
    search_label.pack()
    search_entry.pack()
    search_button.pack()
