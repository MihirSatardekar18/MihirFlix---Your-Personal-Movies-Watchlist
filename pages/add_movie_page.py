import time
import os
import customtkinter as ctk
from PIL import Image
from theme import styled_label, styled_entry, styled_button, PRIMARY_COLOR, ACCENT_ADD, ACCENT_RED, CARD_COLOR, TEXT_COLOR
from utils import storage
from utils.i18n import t

class AddMoviePage(ctk.CTkFrame):
    def __init__(self, master, username, on_done=None):
        super().__init__(master, fg_color="transparent")
        self.username = username
        self.on_done = on_done
        self.poster_preview_img = None

        styled_label(self, t("add_movie"), font=("Segoe UI", 24, "bold"), color=ACCENT_ADD).pack(pady=(10, 20))

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20)

        # Poster preview on left
        self.preview_label = ctk.CTkLabel(container, text="[Poster Preview]", width=200, height=300,
                                          fg_color=CARD_COLOR, text_color=TEXT_COLOR)
        self.preview_label.pack(side="left", padx=(0, 20), pady=10)

        # Form on right
        form_frame = ctk.CTkFrame(container, fg_color="transparent")
        form_frame.pack(side="left", fill="both", expand=True)

        self.title_entry = styled_entry(form_frame, placeholder=t("movie_title"))
        self.title_entry.pack(fill="x", pady=4)

        self.year_entry = styled_entry(form_frame, placeholder=t("year"))
        self.year_entry.pack(fill="x", pady=4)

        # Genre dropdown
        genres = ["Action", "Drama", "Comedy", "Horror", "Romance", "Sci-Fi", "Documentary"]
        self.genre_menu = ctk.CTkOptionMenu(form_frame, values=genres)
        self.genre_menu.set("Select Genre")
        self.genre_menu.pack(fill="x", pady=4)

        # Poster path
        self.poster_entry = styled_entry(form_frame, placeholder=t("poster"))
        self.poster_entry.pack(fill="x", pady=4)
        self.poster_entry.bind("<FocusOut>", lambda e: self._update_poster_preview())

        self.trailer_entry = styled_entry(form_frame, placeholder=t("youtube"))
        self.trailer_entry.pack(fill="x", pady=4)

        # Rating slider 0.0 to 5.0
        slider_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        slider_frame.pack(fill="x", pady=6)
        styled_label(slider_frame, f"{t('rating')} (0.0-5.0):", color=TEXT_COLOR).pack(side="left")
        self.rating_slider = ctk.CTkSlider(slider_frame, from_=0.0, to=5.0, number_of_steps=10, width=200)
        self.rating_slider.set(0.0)
        self.rating_value_label = styled_label(slider_frame, "0.0", color=TEXT_COLOR)
        self.rating_value_label.pack(side="left", padx=10)

        # Live update label when slider moves
        self.rating_slider.configure(command=lambda val: self._update_rating_label(val))

        # Buttons row
        btn_row = ctk.CTkFrame(form_frame, fg_color="transparent")
        btn_row.pack(fill="x", pady=(12, 0))
        styled_button(btn_row, t("save"), self._save, color=PRIMARY_COLOR).pack(side="left", padx=(0, 10))
        styled_button(btn_row, "Back", self._back, color=ACCENT_RED).pack(side="left")

    def _update_rating_label(self, val):
        # Clamp to ensure range safety
        safe_val = max(0.0, min(5.0, float(val)))
        self.rating_value_label.configure(text=f"{safe_val:.1f}")

    def _update_poster_preview(self):
        path = self.poster_entry.get().strip()
        if not path or not os.path.exists(path):
            self.preview_label.configure(image=None, text="[Poster Preview]")
            return
        try:
            img = Image.open(path).resize((200, 300))
            self.poster_preview_img = ctk.CTkImage(img, size=(200, 300))
            self.preview_label.configure(image=self.poster_preview_img, text="")
        except Exception:
            self.preview_label.configure(image=None, text="[Invalid Image]")

    def _save(self):
        # Final clamp before save
        rating_val = max(0.0, min(5.0, round(float(self.rating_slider.get()), 1)))
        movie = {
            "id": f"mv_{int(time.time())}",
            "title": self.title_entry.get().strip(),
            "year": self.year_entry.get().strip(),
            "genre": self.genre_menu.get() if self.genre_menu.get() != "Select Genre" else "",
            "poster_path": self.poster_entry.get().strip(),
            "trailer_url": self.trailer_entry.get().strip(),
            "rating": rating_val
        }
        ok, msg = storage.add_movie(movie)
        self._notify(msg)
        if ok and callable(self.on_done):
            self.on_done()

    def _notify(self, msg):
        from tkinter import messagebox
        messagebox.showinfo("Add Movie", msg)

    def _back(self):
        if callable(self.on_done):
            self.on_done()
