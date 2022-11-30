import tkinter as tk
from tkinter import ttk
import sql_command as sql

class InsertRoomType(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.insert_room_type_container = tk.Frame(self)
        self.insert_room_type_container.place(relx=0.5, rely=0.5, anchor="c")

        self.back_to_menu_button = tk.Button(
            self.insert_room_type_container, text="<- Menu", command=self.back_to_menu)

        self.back_to_menu_button.grid(column=0, row=0)

        self.room_type_name = tk.Label(
            self.insert_room_type_container, text="Room Type")
        self.max_guest = tk.Label(
            self.insert_room_type_container, text="Max guest")
        self.area = tk.Label(
            self.insert_room_type_container, text="Area")
        self.area = tk.Label(
            self.insert_room_type_container, text="Area")

    def back_to_menu(self):
        self.parent.switch_to("MenuScreen")

    def show_customer_table(self):
        pass