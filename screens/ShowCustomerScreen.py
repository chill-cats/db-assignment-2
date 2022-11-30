import tkinter as tk
from tkinter import ttk
import sql_command as sql
from screens.BackButton import BackButton


class ShowCustomerScreen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.back_container = tk.Frame(self)
        self.back_container.pack(fill="x")

        self.back_to_menu_button = BackButton(
            self.back_container, command=self.back_to_menu)

        self.back_to_menu_button.pack(side=tk.LEFT)

        self.table = ttk.Treeview(self, columns=(
            1, 2, 3, 4, 5, 6, 7), show="headings")
        self.table.column(1, anchor=tk.CENTER, width=100, stretch=True)
        self.table.column(2, anchor=tk.CENTER, width=100, stretch=True)
        self.table.column(3, anchor=tk.CENTER, width=100, stretch=True)
        self.table.column(6, anchor=tk.CENTER, width=10, stretch=True)
        self.table.column(7, anchor=tk.CENTER, width=60, stretch=False)
        self.table.heading(1, text="ID",)
        self.table.heading(2, text="CCCD")
        self.table.heading(3, text="Phone")
        self.table.heading(4, text="Email")
        self.table.heading(5, text="Username")
        self.table.heading(6, text="Vip Point")
        self.table.heading(7, text="Class")
        self.table.pack(expand=True, fill="both")

    def before_switch_handler(self):
        self.show_customer_table()

    def back_to_menu(self):
        self.parent.switch_to("MenuScreen")

    def show_customer_table(self):
        for row in self.table.get_children():
            self.table.delete(row)
        if (self.parent.pg_connection != None):
            with self.parent.pg_connection.cursor() as cur:
                cur.execute(sql.show_customer)
                rows = cur.fetchall()
                for row in rows:
                    self.table.insert('', 'end', values=row)