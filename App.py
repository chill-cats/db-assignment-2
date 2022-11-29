import tkinter as tk
from screens.MenuScreen import MenuScreen


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hotel Management")
        self.geometry('800x600')

        self.menu_screen = MenuScreen(self)
        self.menu_screen.pack()
