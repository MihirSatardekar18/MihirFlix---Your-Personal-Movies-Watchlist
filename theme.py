import os
import customtkinter as ctk
from PIL import Image

PRIMARY_COLOR = "#7C3AED"
SECONDARY_COLOR = "#06B6D4"
BACKGROUND_COLOR = "#0B0F19"
CARD_COLOR = "#121726"
TEXT_COLOR = "#E6ECF3"
SUBTEXT_COLOR = "#A7B0C0"
BORDER_COLOR = "#1C2336"

ACCENT_GREEN = "#22C55E"
ACCENT_RED = "#EF4444"
ACCENT_AMBER = "#F59E0B"
ACCENT_BLUE = "#60A5FA"
ACCENT_PINK = "#F472B6"
ACCENT_YELLOW = "#FBBF24"
ACCENT_VIOLET = "#A78BFA"
ACCENT_LIGHTBLUE = "#38BDF8"
ACCENT_TEAL = "#14B8A6"
ACCENT_ROSE = "#FB7185"

ACCENT_LOGIN = "#22D3EE"
ACCENT_REGISTER = ACCENT_ROSE
ACCENT_HOME = ACCENT_TEAL
ACCENT_WATCHLIST = ACCENT_BLUE
ACCENT_ADD = ACCENT_GREEN
ACCENT_SETTINGS = ACCENT_YELLOW
ACCENT_PROFILE = ACCENT_VIOLET
ACCENT_ABOUT = ACCENT_PINK
ACCENT_CONTACT = ACCENT_LIGHTBLUE
ACCENT_STATS = "#8B5CF6"

TITLE_FONT = ("Segoe UI", 26, "bold")
SUBTITLE_FONT = ("Segoe UI", 18, "bold")
BODY_FONT = ("Segoe UI", 14)
BUTTON_FONT = ("Segoe UI", 14, "bold")

ASSETS_DIR = os.path.join("assets")
UI_DIR = os.path.join(ASSETS_DIR, "ui")
POSTERS_DIR = os.path.join(ASSETS_DIR, "posters")
LOGO_PATH = os.path.join(UI_DIR, "logo.png")
BANNER_PATH = os.path.join(UI_DIR, "banner.jpg")

def apply_theme(root):
    root.configure(fg_color=BACKGROUND_COLOR)

def styled_button(master, text, command=None, color=PRIMARY_COLOR):
    return ctk.CTkButton(
        master, text=text, command=command, fg_color=color,
        hover_color=_darken(color, 0.12), font=BUTTON_FONT,
        text_color="white", corner_radius=10, height=40
    )

def styled_label(master, text, font=BODY_FONT, color=TEXT_COLOR):
    return ctk.CTkLabel(master, text=text, font=font, text_color=color)

def styled_entry(master, placeholder=""):
    return ctk.CTkEntry(
        master, placeholder_text=placeholder, font=BODY_FONT,
        fg_color=CARD_COLOR, text_color=TEXT_COLOR,
        placeholder_text_color=SUBTEXT_COLOR,
        border_width=1, corner_radius=8, border_color=BORDER_COLOR
    )

def accent_for(key: str) -> str:
    return {
        "login": ACCENT_LOGIN,
        "register": ACCENT_REGISTER,
        "home": ACCENT_HOME,
        "watchlist": ACCENT_WATCHLIST,
        "add_movie": ACCENT_ADD,
        "settings": ACCENT_SETTINGS,
        "profile": ACCENT_PROFILE,
        "about": ACCENT_ABOUT,
        "contact": ACCENT_CONTACT,
        "stats": ACCENT_STATS,
    }.get(key, PRIMARY_COLOR)

def _hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def _rgb_to_hex(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return f"#{r:02x}{g:02x}{b:02x}"

def _darken(color, factor=0.15):
    r, g, b = _hex_to_rgb(color)
    return _rgb_to_hex(int(r*(1-factor)), int(g*(1-factor)), int(b*(1-factor)))

def load_image(path: str, size: tuple[int, int] | None = None):
    if not path or not os.path.exists(path):
        return None
    try:
        img = Image.open(path)
        if size:
            img = img.resize(size)
        return ctk.CTkImage(img, size=size) if size else ctk.CTkImage(img)
    except Exception:
        return None
