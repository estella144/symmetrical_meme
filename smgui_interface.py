# This file is part of Symmetrical Meme
# A task management application in Python
# v0.2.dev3 (2 Sep 2023, main/857f324)

# Summary:
# A Python CLI task management application
# with CRUD operations for tasks, data storage, and error handling.

from smcrud import add_task, list_tasks, update_task, delete_task, search_tasks

# Function to add a task (you'll need to implement this)
def add_task():
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
        add_task(title, description, due_date, priority)  # Pass priority to add_task

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
def list_tasks():
    # Placeholder function for listing tasks
    messagebox.showinfo("List Tasks", "Functionality to list tasks will be implemented here.")
