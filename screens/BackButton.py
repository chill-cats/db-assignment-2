import tkinter as tk


class BackButton(tk.Button):
    def __init__(self, master, command, *args, **kwargs):
        super().__init__(master, text="Back", command=command, *args, **kwargs)
