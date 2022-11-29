import tkinter as tk
from screens.MenuScreen import MenuScreen
from screens.LoginScreen import LoginScreen
import psycopg.errors as pg_errors
import psycopg as pg
import tomli


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

        self.menu_screen = MenuScreen(self)
        self.menu_screen.place(in_=self, x=0, y=0, relwidth=1, relheight=1)

        self.login_screen = LoginScreen(self)
        self.login_screen.place(in_=self, x=0, y=0, relwidth=1, relheight=1)

    def login(self, username: str, password: str):
        print(f"Connecting with {username}, {password}")
        try:
            pg_connection = pg.connect(
                f"host={self.app_config['postgres']['ip']} user={username} password={password}")
        except pg_errors.OperationalError as e:
            print(e)
        return None
