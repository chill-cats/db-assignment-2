import tkinter as tk
from tkinter import ttk
import sql_command as sql
from screens.BackButton import BackButton
import tkinter.messagebox as messagebox


class ShowTotalGuest(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.back_container = tk.Frame(self)
        self.back_container.pack(fill="x")

        self.back_to_total_guest_button = BackButton(
            self.back_container, command=self.back_to_total_guest)

        self.back_to_total_guest_button.pack(side=tk.LEFT)

        self.table = ttk.Treeview(self, columns=(
            1, 2), show="headings")
        self.table.column(1, anchor=tk.CENTER, width=100, stretch=True)
        self.table.column(2, anchor=tk.CENTER, width=100, stretch=True)
        self.table.heading(1, text="Month",)
        self.table.heading(2, text="Total Guest")

        self.table.pack(expand=True, fill="both")

    def before_switch_handler(self):
        self.show_statistic_table()

    def back_to_total_guest(self):
        self.parent.reload_total_guest()
    
    def show_statistic_table(self):
        for row in self.table.get_children():
            self.table.delete(row)
        if (self.parent.return_pg_connection() != None):
            with self.parent.return_pg_connection().cursor() as cur:
                branch = self.parent.branch.get()
                year = self.parent.year.get()
                if (branch == "" or year == ""):
                    messagebox.showerror(message="Branch ID and year is required")
                    return
                try: 
                    int(year)
                except:
                    messagebox.showerror(message="Year must be an integer")
                    return
                cur.execute(sql.show_total_guest, {"branch": branch, "year": year})
                rows = cur.fetchall()
                for row in rows:
                    self.table.insert('', 'end', values=row)
