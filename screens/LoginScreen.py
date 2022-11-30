import tkinter as tk
import tkinter.messagebox as messagebox


class LoginScreen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.user_name = tk.StringVar(self)
        self.password = tk.StringVar(self)

        self.login_form_container = tk.Frame(self)

        self.user_name_label = tk.Label(
            self.login_form_container, text="Username")
        self.user_name_entry = tk.Entry(
            self.login_form_container, textvariable=self.user_name)

        self.password_label = tk.Label(
            self.login_form_container, text="Password")
        self.password_entry = tk.Entry(
            self.login_form_container, textvariable=self.password, show="•")

        self.login_button = tk.Button(
            self.login_form_container, text="Login", command=self.login_handler)

        self.user_name_label.grid(column=0, row=0, padx=(20, 20))
        self.user_name_entry.grid(column=1, row=0, pady=(20, 10))
        self.password_label.grid(column=0, row=1, padx=(20, 20))
        self.password_entry.grid(column=1, row=1, pady=(10, 0))
        self.login_button.grid(column=1, row=2, pady=(20, 20))

        self.login_form_container.place(relx=0.5, rely=0.5, anchor="c")

    def login_handler(self):
        username = self.user_name.get()
        password = self.password.get()
        if username == "" or password == "":
            messagebox.showerror(message="Username and password is required")
            return
        self.parent.login(username, password)
