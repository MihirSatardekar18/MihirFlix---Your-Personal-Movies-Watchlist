import customtkinter as ctk
from theme import styled_label, PRIMARY_COLOR, BACKGROUND_COLOR, styled_button
from utils.i18n import t

# Define a colour palette for sidebar buttons
NAV_COLORS = {
    "home":         "#1E90FF",  # DodgerBlue
    "watchlist":    "#FF8C00",  # DarkOrange
    "add_movie":    "#32CD32",  # LimeGreen
    "profile":      "#9370DB",  # MediumPurple
    "about":        "#00CED1",  # DarkTurquoise
    "contact":      "#FF1493",  # DeepPink
    "stats":        "#DC143C",  # GoldCrimson Luxe
}

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, on_nav, username):
        super().__init__(master, fg_color=BACKGROUND_COLOR, width=220)
        self.on_nav = on_nav
        self.username = username
        self._build_ui()

    def _build_ui(self):
        styled_label(self, "🎬 MihirFlix", font=("Segoe UI", 22, "bold"),
                     color=PRIMARY_COLOR).pack(pady=(18, 6))
        styled_label(self, f"{t('welcome')}, {self.username}!", font=("Segoe UI", 14),
                     color="#AAAAAA").pack(pady=(0, 16))

        nav = [
            (t("home"), "home"),
            (t("watchlist"), "watchlist"),
            (t("add_movie"), "add_movie"),
            (t("profile"), "profile"),
            (t("about"), "about"),
            (t("contact"), "contact"),
            (t("stats"), "stats"),
        ]
        for label, key in nav:
            color = NAV_COLORS.get(key, "#444444")  # default fallback
            btn = ctk.CTkButton(
                self,
                text=label,
                command=lambda k=key: self.on_nav(k),
                fg_color=color,
                hover_color=self._darken(color, 0.85),  # custom hover shade
                text_color="white",
                corner_radius=8,
                font=("Segoe UI", 14, "bold")
            )
            btn.pack(fill="x", padx=12, pady=6)

    def _darken(self, hex_color, factor=0.8):
        """ Darkens a HEX color for hover effect """
        hex_color = hex_color.lstrip("#")
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        darkened = tuple(int(c * factor) for c in rgb)
        return "#%02x%02x%02x" % darkened
