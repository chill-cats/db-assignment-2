import tkinter as tk
from screens.MenuScreen import MenuScreen
from screens.LoginScreen import LoginScreen
import psycopg.errors as pg_errors
import psycopg as pg
import tomli
import tkinter.messagebox as messagebox
from enum import Enum
from typing import Optional


def load_config():
    with open("config.toml", mode="rb") as config_file:
        config = tomli.load(config_file)
    return config


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Load config
        self.app_config = load_config()

        # Window creation
        self.title("Hotel Management")
        self.geometry('800x600')
        self.resizable(0, 0)

        self.sub_screens = [MenuScreen(self), LoginScreen(self)]
        for screen in self.sub_screens:
            screen.place(in_=self, x=0, y=0, relwidth=1, relheight=1)

        self.pg_connection: Optional[pg.Connection] = None

    def switch_to(self, screen: str):
        match screen:
            case "MenuScreen":
                self.sub_screens[0].tkraise()
            case "LoginScreen":
                self.sub_screens[1].tkraise()
            case _:
                raise ValueError(
                    f"screen must be one of \"MenuScreen\" or \"LoginScreen\", recived {screen}")

    def login(self, username: str, password: str):
        print(f"Connecting with {username}, {password}")
        try:
            self.pg_connection = pg.connect(
                f"host={self.app_config['postgres']['ip']} user={username} password={password}")
        except pg_errors.OperationalError as e:
            err_message = str(e)
            messagebox.showerror(
                message=f"Cannot connect to database with error {err_message}")
            return
        self.switch_to("MenuScreen")
