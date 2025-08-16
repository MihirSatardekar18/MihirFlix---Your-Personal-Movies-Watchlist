import os
import customtkinter as ctk
from utils import storage
from PIL import Image
from theme import SUBTEXT_COLOR

PRIMARY_COLOR = "#ff9800"
REMOVE_COLOR = "#d32f2f"
DELETE_COLOR = "#9c27b0"
WATCHED_COLOR = "#4caf50"

class MovieCard(ctk.CTkFrame):
    def __init__(self, master, movie, username, refresh_callback=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.username = username
        self.movie = movie if isinstance(movie, dict) else {}
        self.refresh_callback = refresh_callback
        self._build_ui()

    def _build_ui(self):
        mid = self.movie.get("id")
        title = self.movie.get("title", "Unknown Title")
        year = self.movie.get("year", "")
        genre = self.movie.get("genre", "—")
        trailer_url = (self.movie.get("trailer_url") or "").strip()
        poster_path = (self.movie.get("poster_path") or "").strip()

        img = None
        if poster_path and os.path.exists(poster_path):
            try:
                img = ctk.CTkImage(Image.open(poster_path), size=(100, 150))
            except Exception:
                pass

        row = ctk.CTkFrame(self)
        row.pack(fill="x", padx=6, pady=4)

        if img:
            ctk.CTkLabel(row, image=img, text="").pack(side="left", padx=6)
        else:
            ctk.CTkLabel(row, text="[No Poster]", width=100, height=150).pack(side="left", padx=6)

        details = ctk.CTkFrame(row)
        details.pack(side="left", fill="both", expand=True)
        ctk.CTkLabel(details, text=f"{title} ({year})", font=("Arial", 16, "bold")).pack(anchor="w")
        ctk.CTkLabel(details, text=f"Genre: {genre}", font=("Arial", 12), text_color=SUBTEXT_COLOR).pack(anchor="w")

        btn_row = ctk.CTkFrame(details)
        btn_row.pack(anchor="w", pady=4)

        if mid:
            watched = storage.is_watched(self.username, mid)
            watch_text = "Unmark Watched" if watched else "Mark as Watched"
            ctk.CTkButton(
                btn_row, text=watch_text, fg_color=WATCHED_COLOR,
                command=lambda: self._toggle_watched(mid)
            ).pack(side="left", padx=4)

            in_watchlist = any(m.get("id") == mid for m in storage.list_watchlist_movies(self.username))
            wl_text = "Remove from Watchlist" if in_watchlist else "Add to Watchlist"
            wl_cmd = storage.remove_from_watchlist if in_watchlist else storage.add_to_watchlist
            ctk.CTkButton(
                btn_row, text=wl_text, fg_color=PRIMARY_COLOR,
                command=lambda: self._wrap(wl_cmd, mid)
            ).pack(side="left", padx=4)

            ctk.CTkButton(
                btn_row, text="Delete", fg_color=DELETE_COLOR,
                command=lambda: self._delete(mid)
            ).pack(side="left", padx=4)

        if trailer_url:
            ctk.CTkButton(
                btn_row, text="Trailer", fg_color="#2196f3",
                command=lambda: storage.open_trailer(trailer_url)
            ).pack(side="left", padx=4)

    def _wrap(self, fn, mid):
        if fn in (storage.add_to_watchlist, storage.remove_from_watchlist):
            fn(self.username, mid)
        else:
            fn(mid)
        if self.refresh_callback:
            self.refresh_callback()

    def _toggle_watched(self, mid):
        storage.toggle_watched(self.username, mid)
        if self.refresh_callback:
            self.refresh_callback()

    def _delete(self, mid):
        storage.delete_movie(mid)
        storage.remove_from_watchlist(self.username, mid)
        if self.refresh_callback:
            self.refresh_callback()
