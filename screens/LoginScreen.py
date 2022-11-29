import tkinter as tk


class LoginScreen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.password = tk.StringVar(self)
        self.login_entry_label = tk.Label(self, text="Username")
        self.login_entry_label.pack()
        self.login = tk.Entry(self, textvariable=self.password)
        self.login.pack()
