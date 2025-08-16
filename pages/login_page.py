import customtkinter as ctk
from theme import styled_label, styled_entry, styled_button, TITLE_FONT, PRIMARY_COLOR, ACCENT_LOGIN, ACCENT_GREEN, ACCENT_RED
from utils.i18n import t
from utils import storage

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, go_register, go_home):
        super().__init__(master, fg_color="transparent")
        self.go_register = go_register
        self.go_home = go_home

        styled_label(self, t("welcome"), font=TITLE_FONT, color=ACCENT_LOGIN).pack(pady=(60, 10))
        self.username_entry = styled_entry(self, placeholder="Username")
        self.username_entry.pack(pady=6)
        self.password_entry = styled_entry(self, placeholder="Password")
        self.password_entry.configure(show="*")
        self.password_entry.pack(pady=6)

        self.msg_label = styled_label(self, "", color=ACCENT_RED)
        self.msg_label.pack(pady=6)

        styled_button(self, "Login", command=self._login, color=ACCENT_LOGIN).pack(pady=6)
        styled_button(self, "Register", command=self.go_register, color=PRIMARY_COLOR).pack(pady=6)

        self.bind("<Return>", lambda e: self._login())

    def _login(self):
        u = self.username_entry.get().strip()
        p = self.password_entry.get().strip()
        ok, msg = storage.validate_login(u, p)
        if ok:
            self.msg_label.configure(text=msg, text_color=ACCENT_GREEN)
            self.after(500, lambda: self.go_home(u))
        else:
            self.msg_label.configure(text=msg, text_color=ACCENT_RED)
