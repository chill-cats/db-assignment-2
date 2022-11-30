import tkinter as tk
from tkinter import ttk
import sql_command as sql
import psycopg
import tkinter.messagebox as messagebox
from screens.BackButton import BackButton


class InsertRoomType(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        

        self.back_to_menu_button = BackButton(
            self, command=self.back_to_menu)
        self.back_to_menu_button.grid(column=0, row=0)

        self.room_type_name = tk.StringVar(self)
        self.room_type_name_label = tk.Label(
            self, text="Room type name")
        self.room_type_name_entry = tk.Entry(
            self, textvariable=self.room_type_name)
        
        self.max_guest = tk.StringVar(self)
        self.max_guest_label = tk.Label(
            self, text="Max guest")
        self.max_guest_entry = tk.Entry(
            self, textvariable=self.max_guest)
        
        self.area = tk.StringVar(self)
        self.area_label = tk.Label(
            self, text="Area")
        self.area_entry = tk.Entry(
            self, textvariable=self.area)

        self.insert_room_type_button = tk.Button(
            self, text="Insert", command=self.insert_to_database)

        self.description = tk.StringVar(self)
        self.description_label = tk.Label(
            self, text="Description")
        self.description_entry = tk.Entry(
            self, textvariable=self.description)

        self.size = tk.StringVar(self)
        self.size_label = tk.Label(
            self, text="Bed size"
        )
        self.size_entry = tk.Entry(
            self, textvariable=self.size)

        self.count = tk.StringVar(self)
        self.count_label = tk.Label(
            self, text="Count"
        )
        self.count_entry = tk.Entry(
            self, textvariable=self.count)

        self.material_type_id = tk.StringVar(self)
        self.material_label = tk.Label(
            self, text="Material Type ID"
        )
        self.material_entry = tk.Entry(
            self, textvariable=self.material_type_id)

        self.material_amount = tk.StringVar(self)
        self.material_amount_label = tk.Label(
            self, text="Material amount"
        )
        self.material_amount_entry = tk.Entry(
            self, textvariable=self.material_amount)


        self.back_to_menu_button.grid(column=0, row=0)
        self.room_type_name_label.grid(column=0, row=1)
        self.room_type_name_entry.grid(column=1, row=1)
        self.max_guest_label.grid(column=0, row=2)
        self.max_guest_entry.grid(column=1, row=2)
        self.area_label.grid(column=0, row=3)
        self.area_entry.grid(column=1, row=3)
        self.description_label.grid(column=0, row=4)
        self.description_entry.grid(column=1, row=4)
        self.size_label.grid(column=0, row=5)
        self.size_entry.grid(column=1, row=5)
        self.count_label.grid(column=0, row=6)
        self.count_entry.grid(column=1, row=6)
        self.material_label.grid(column=0, row=7)
        self.material_entry.grid(column=1, row=7)
        self.material_amount_label.grid(column=0, row=8)
        self.material_amount_entry.grid(column=1, row=8)
        self.insert_room_type_button.grid(column=0, row=9)

    def insert_to_database(self):
        room_type_name = self.room_type_name.get()
        conn = self.parent.pg_connection.execute(
            "INSERT INTO \"RoomType\" (room_type_name, max_guest, area, description) VALUES (%s, %s, %s, %s)",
            (room_type_name, self.max_guest.get(), self.area.get(), self.description.get())
        )
        self.parent.pg_connection.execute(
            "SELECT room_type_id FROM \"RoomType\" WHERE (room_type_name = %s)",
            (room_type_name)
        )
        print(self.parent.pg_connection.fetchone())
        if conn:
            messagebox.showinfo(
                message=f"Successful insert to the database !")
        self.parent.pg_connection.commit()

    def back_to_menu(self):
        self.parent.switch_to("MenuScreen")

    def show_customer_table(self):
        pass

    def before_switch_handler(self):
        pass
