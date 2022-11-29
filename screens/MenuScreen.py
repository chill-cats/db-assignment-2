import tkinter as tk


class MenuScreen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.password = tk.StringVar(self)
        self.login = tk.Entry(self, textvariable=self.password)
        self.login.pack()
