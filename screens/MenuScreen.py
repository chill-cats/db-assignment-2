import tkinter as tk


class MenuScreen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.menu_form_container = tk.Frame(self)
        self.menu_form_container.place(x=0, y=0)

        self.show_customer_button = tk.Button(
            self.menu_form_container, text="Show customer", command=self.show_customer_handler)

        self.insert_room_type_button = tk.Button(
            self.menu_form_container, text="Insert room type", command=self.insert_room_type_handler)

        self.show_customer_button.grid(column=0, row=0)
        self.insert_room_type_button.grid(column=1, row=0)

    def show_customer_handler(self):
        self.parent.switch_to("ShowCustomerScreen")

    def insert_room_type_handler(self):
        self.parent.switch_to("InsertRoomType")