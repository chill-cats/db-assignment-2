import tkinter as tk
from tkinter import ttk
import sql_command as sql
from screens.BackButton import BackButton


class InsertRoomType(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.back_to_menu_button = BackButton(
            self, command=self.back_to_menu)

        self.back_to_menu_button.grid(column=0, row=0)

    def back_to_menu(self):
        self.parent.switch_to("MenuScreen")

    def show_customer_table(self):
        pass

    def before_switch_handler(self):
        pass
