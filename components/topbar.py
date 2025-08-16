# components/topbar.py
import customtkinter as ctk

class TopBar(ctk.CTkFrame):
    def __init__(self, master, title_text: str, accent_color: str):
        super().__init__(master, fg_color="transparent")
        self.label = ctk.CTkLabel(self, text=title_text,
                                  font=("Segoe UI", 20, "bold"),
                                  text_color=accent_color)
        self.label.pack(anchor="w", padx=16)
