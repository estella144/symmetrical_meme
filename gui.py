# This file is part of TaskFlow
# A task management application in Python
# v0.3 (3 Sep 2023, main/79fddc2)

# Summary:
# A Python CLI task management application
# with CRUD operations for tasks, data storage, and error handling.

import tkinter as tk
from tkinter import messagebox
from gui_interface import add_task_gui, list_tasks_gui, update_task_gui, delete_task_gui, search_tasks_gui

# Create the main application window
root = tk.Tk()
root.title("TaskFlow")

def quit_application():
    root.destroy()  # Close the main application window

# Create GUI elements
add_button = tk.Button(root, text="Add Task", command=add_task_gui)
list_button = tk.Button(root, text="List Tasks", command=list_tasks_gui)
update_button = tk.Button(root, text="Update Task", command=update_task_gui)
delete_button = tk.Button(root, text="Delete Task", command=delete_task_gui)
search_button = tk.Button(root, text="Search Tasks", command=search_tasks_gui)
quit_button = tk.Button(root, text="Quit", command=quit_application)


# Pack the elements onto the window
add_button.pack()
list_button.pack()
update_button.pack()
delete_button.pack()
search_button.pack()
quit_button.pack()

# Start the GUI application
root.mainloop()
