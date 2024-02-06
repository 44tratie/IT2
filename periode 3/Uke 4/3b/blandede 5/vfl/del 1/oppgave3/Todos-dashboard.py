import tkinter as tk
from tkinter import ttk

from modeller.ToDoTaskListModell_copy import ToDoList

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDoList App")

        # Oppretter en instance av klasen ToDoList. Klassen innholder en liste med 
        # instanser av ToDoTask. Konstruktor tar in en parameter navnet på json filen
        # med ToDo-oppgaver
        self.toDoList = ToDoList("todos.json")     

        #Oppretter grafisk grensesnitt og viser TODO-listen  
        self.create_gui()

    def create_gui(self):
        # Frame for user ID filter
        user_filter_frame = ttk.Frame(self.root)
        user_filter_frame.pack(pady=10)

        ttk.Label(user_filter_frame, text="User ID:").grid(row=0, column=0, padx=5)
        self.user_id_entry = ttk.Entry(user_filter_frame)
        self.user_id_entry.grid(row=0, column=1, padx=5)

        # Frame for completed filter
        completed_filter_frame = ttk.Frame(self.root)
        completed_filter_frame.pack(pady=10)

        #self.completed_var = tk.BooleanVar()
        self.completed_var = tk.IntVar(value=None)
        ttk.Checkbutton(completed_filter_frame, text="Show Completed", variable=self.completed_var).pack(side=tk.LEFT, padx=5)


        # Treeview for displaying tasks
        self.tree = ttk.Treeview(self.root, columns=("ID", "Owner", "Title", "Completed"), show="headings")
        self.tree.column
        self.tree.heading("ID", text="ID")
        self.tree.heading("Owner", text="Owner")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Completed", text="Completed")

        for task in self.toDoList.Tasks():
            self.tree.insert("", "end", values=(task.id, task.owner, task.title, task.completed))

        self.tree.pack(expand=True, fill=tk.BOTH)

        # Button for applying filters
        ttk.Button(self.root, text="Apply Filters", command=self.apply_filters).pack(pady=10)

         # Button for reset
        ttk.Button(self.root, text="Remove All Filters", command=self.remove_all_filters).pack(pady=10)

    def remove_all_filters(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Hent 
        for task in self.toDoList.Tasks():
             self.tree.insert("", "end", values=(task.id, task.owner, task.title, task._completed))
           
    def apply_filters(self):
        # Get filter values
        user_id_filter = self.user_id_entry.get()     # the userId, "" when not set
        completed_filter = self.completed_var.get()   # a bool value, false when not set

        # Apply filters and repopulate the treeview
        
        # Clear existing items in the treeview
        for item in self.tree.get_children():
          self.tree.delete(item)
        # Hent 
        if not user_id_filter: user_id_filter = -1

        for task in self.toDoList.Tasks( int(completed_filter), int(user_id_filter),):
             self.tree.insert("", "end", values=(task.id, task.owner, task.title, task._completed))
           
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
