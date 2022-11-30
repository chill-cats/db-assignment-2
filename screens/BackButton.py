import tkinter as tk


class BackButton(tk.Button):
    def __init__(self, master, command, *args, **kwargs):
        super().__init__(master, text="Back", bg="black", command=command, *args, **kwargs)
