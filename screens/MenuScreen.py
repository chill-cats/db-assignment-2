import tkinter as tk


class MenuScreen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.show_customer_button = tk.Button(
            self, text="Show customer", command=self.show_customer_handler)

        self.insert_room_type_button = tk.Button(
            self, text="Insert room type", command=self.insert_room_type_handler)

        self.total_guest_button = tk.Button(
            self, text="Total guest", command=self.total_guest_handler)

        self.sign_out_button = tk.Button(
            self, text="Sign out", command=self.sign_out_handler)

        self.show_customer_button.grid(column=0, row=0)
        self.insert_room_type_button.grid(column=1, row=0)
        self.total_guest_button.grid(column=2, row=0)
        self.sign_out_button.grid(column=3, row=0)

    def show_customer_handler(self):
        self.parent.switch_to("ShowCustomerScreen")

    def insert_room_type_handler(self):
        self.parent.switch_to("InsertRoomType")

    def total_guest_handler(self):
        self.parent.switch_to("TotalGuest")
    
    def sign_out_handler(self):
        self.parent.switch_to("LoginScreen")
        self.parent.pg_connection.close()
        self.parent.pg_connection = None
        self.parent.sub_screens[1].password.set("")
        self.parent.sub_screens[1].user_name.set("")

    def before_switch_handler(self):
        pass
