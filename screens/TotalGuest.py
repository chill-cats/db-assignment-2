import tkinter as tk
from tkinter import ttk
import sql_command as sql
from screens.BackButton import BackButton
from screens.ShowTotalGuest import ShowTotalGuest

class TotalGuest(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.back_container = tk.Frame(self)
        self.back_container.pack(fill="x")

        self.back_to_menu_button = BackButton(
            self.back_container, command=self.back_to_menu)

        self.back_to_menu_button.pack(side=tk.LEFT)

        #self.table = ttk.Treeview(self, columns=(
        #    1, 2), show="headings")
        #self.table.column(1, anchor=tk.CENTER, width=100, stretch=True)
        #self.table.column(2, anchor=tk.CENTER, width=100, stretch=True)
        #self.table.heading(1, text="Month",)
        #self.table.heading(2, text="Total guest")
        # self.table.grid(column=0, row=1)
        #self.table.pack(expand=True, fill="both")
        self.branch = tk.StringVar(self)
        self.year = tk.StringVar(self)

        self.query_form_container = tk.Frame(self)
        self.query_form_container.place(relx=0.5, rely=0.5, anchor="c")

        self.branch_label = tk.Label(
            self.query_form_container, text="Branch")
        self.branch_entry = tk.Entry(
            self.query_form_container, textvariable=self.branch)

        self.year_label= tk.Label(
            self.query_form_container, text="Year")
        self.year_entry= tk.Entry(
            self.query_form_container, textvariable=self.year)

        self.query_button = tk.Button(
            self.query_form_container, text="Search", command=self.query_handler)

        self.branch_label.grid(column=0, row=0, padx=(20, 20))
        self.branch_entry.grid(column=1, row=0, pady=(20, 10))
        self.year_label.grid(column=0, row=1, padx=(20, 20))
        self.year_entry.grid(column=1, row=1, pady=(10, 0))
        self.query_button.grid(column=1, row=2, pady=(20, 20))



    def back_to_menu(self):
        self.parent.switch_to("MenuScreen")
    
    def reload_total_guest(self):
        self.sub_screens.destroy()
        self.parent.switch_to("TotalGuest")
    
    def query_handler(self):
        self.sub_screens = ShowTotalGuest(self)
        self.sub_screens.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        self.sub_screens.before_switch_handler()
        self.sub_screens.tkraise()
    
    def return_pg_connection(self):
        return self.parent.pg_connection

    def before_switch_handler(self):
        pass