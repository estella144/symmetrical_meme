# This file is part of Symmetrical Meme
# A task management application in Python
# v0.2.dev4 (2 Sep 2023, main/bfdf685)

# Summary:
# A Python CLI task management application
# with CRUD operations for tasks, data storage, and error handling.

import tkinter as tk
from tkinter import messagebox
from smgui_interface import add_task_gui, list_tasks_gui

# Create the main application window
root = tk.Tk()
root.title("Symmetrical Meme")

# Create GUI elements
add_button = tk.Button(root, text="Add Task", command=add_task_gui)
list_button = tk.Button(root, text="List Tasks", command=list_tasks_gui)

# Pack the elements onto the window
add_button.pack()
list_button.pack()

# Start the GUI application
root.mainloop()
