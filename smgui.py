# This file is part of Symmetrical Meme
# A task management application in Python
# v0.2.dev2 (2 Sep 2023, main/857f324)

# Summary:
# A Python CLI task management application
# with CRUD operations for tasks, data storage, and error handling.

import tkinter as tk
from tkinter import messagebox
from smgui_interface import add_task, list_tasks

# Create the main application window
root = tk.Tk()
root.title("Symmetrical Meme Task Manager")

# Create GUI elements
add_button = tk.Button(root, text="Add Task", command=add_task_gui)
list_button = tk.Button(root, text="List Tasks", command=list_tasks_gui)

# Pack the elements onto the window
add_button.pack()
list_button.pack()

# Start the GUI application
root.mainloop()
