import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Task entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add task button
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()

        # Task list
        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.pack(pady=10)

        # Remove task button
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()


