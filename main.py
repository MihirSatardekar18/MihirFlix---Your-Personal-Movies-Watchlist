import customtkinter as ctk
from utils import storage
from utils.config import APP_WIDTH, APP_HEIGHT
from theme import apply_theme
from pages.login_page import LoginPage
from utils.auto_heal_movies import auto_heal_movies_json

auto_heal_movies_json()
storage.init_storage()
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class MihirFlixApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MihirFlix - Yours Personal Movies Watchlist App 😎")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.resizable(True, True)
        apply_theme(self)
        self._show_login()

    def _clear(self):
        for w in self.winfo_children():
            w.destroy()

    def _show_login(self): 
        self._clear()
        self.login_page = LoginPage(self, self._show_register, self._show_home)
        self.login_page.pack(fill="both", expand=True)

    def _show_register(self):
        self._clear()
        from pages.register_page import RegisterPage
        self.register_page = RegisterPage(self, self._show_login)
        self.register_page.pack(fill="both", expand=True)

    def _show_home(self, username):
        self._clear()
        from pages.homepage import HomePage
        self.home_page = HomePage(self, username, on_logout=self._show_login)
        self.home_page.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MihirFlixApp()
    app.mainloop()
