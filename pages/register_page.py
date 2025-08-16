import customtkinter as ctk
from theme import styled_label, styled_entry, styled_button, TITLE_FONT, ACCENT_REGISTER, PRIMARY_COLOR, ACCENT_RED, ACCENT_GREEN
from utils import storage

class RegisterPage(ctk.CTkFrame):
    def __init__(self, master, go_login):
        super().__init__(master, fg_color="transparent")
        self.go_login = go_login

        styled_label(self, "Create Account", font=TITLE_FONT, color=ACCENT_REGISTER).pack(pady=(50, 10))
        self.username_entry = styled_entry(self, placeholder="Username")
        self.username_entry.pack(pady=6)
        self.password_entry = styled_entry(self, placeholder="Password")
        self.password_entry.configure(show="*")
        self.password_entry.pack(pady=6)

        self.msg_label = styled_label(self, "", color=ACCENT_RED)
        self.msg_label.pack(pady=6)

        styled_button(self, "Register", command=self._handle_register, color=ACCENT_REGISTER).pack(pady=6)
        styled_button(self, "Back to Login", command=self.go_login, color=PRIMARY_COLOR).pack(pady=6)

        self.bind("<Return>", lambda e: self._handle_register())

    def _handle_register(self):
        u = self.username_entry.get().strip()
        p = self.password_entry.get().strip()
        ok, msg = storage.register_user(u, p)
        self.msg_label.configure(text=msg, text_color=ACCENT_GREEN if ok else ACCENT_RED)
        if ok:
            self.after(600, self.go_login)
