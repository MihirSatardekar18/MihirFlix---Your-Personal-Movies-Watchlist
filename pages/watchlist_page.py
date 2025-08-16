import customtkinter as ctk
import webbrowser
from utils import storage
from components.movie_card import MovieCard
from utils.i18n import t
from theme import accent_for, styled_label, styled_button

class WatchlistPage(ctk.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master, fg_color="transparent")
        self.username = username
        self.selected_genre = t("all")
        self._render()

    def _render(self):
        for w in self.winfo_children():
            w.destroy()
        self._render_header()
        self._render_list()

    def _render_header(self):
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=16, pady=(8, 6))

        styled_label(header, t("watchlist_title"), font=("Segoe UI", 20, "bold"),
                     color=accent_for("watchlist")).pack(side="left")

        right = ctk.CTkFrame(header, fg_color="transparent")
        right.pack(side="right")

        if self.selected_genre != t("all"):
            styled_label(right, f"{t('filter_by_genre')}: {self.selected_genre}",
                         color="white", font=("Segoe UI", 14, "bold")).pack(side="left", padx=(0, 10))
            styled_button(right, t("clear"), self._clear_genre, color="#6B7280").pack(side="left", padx=(0, 10))
        styled_button(right, t("select_genre"), self._open_genre_picker, color=accent_for("watchlist")).pack(side="left")

    def _render_list(self):
        # Destroy everything except header
        for w in list(self.winfo_children())[1:]:
            w.destroy()

        sc = ctk.CTkScrollableFrame(self, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=16, pady=10)

        movies = storage.list_watchlist_movies(self.username)
        if self.selected_genre != t("all"):
            sel = (self.selected_genre or "").strip().lower()
            movies = [m for m in movies if (m.get("genre") or "").strip().lower() == sel]

        if not movies:
            styled_label(sc, t("empty_watchlist"), color="#A7B0C0").pack(pady=20)
            return

        for m in movies[::-1]:
            # MovieCard + trailer button wrapper
            card_frame = ctk.CTkFrame(sc, fg_color="transparent")
            card_frame.pack(fill="x", pady=6, padx=4)

            MovieCard(card_frame, m, self.username, refresh_callback=self._render).pack(side="left", fill="x", expand=True)

           
    def _clear_genre(self):
        self.selected_genre = t("all")
        self._render()

    def _open_genre_picker(self):
        gens = self._genres_with_counts()
        total = sum(cnt for _, cnt in gens)
        win = ctk.CTkToplevel(self)
        win.title(t("choose_genre"))
        win.geometry("400x500")
        win.transient(self.winfo_toplevel()); win.grab_set()
        win.resizable(False, False)

        wrapper = ctk.CTkFrame(win, fg_color="transparent")
        wrapper.pack(fill="both", expand=True, padx=14, pady=12)

        styled_label(wrapper, t("filter_by_genre"), font=("Segoe UI", 18, "bold"),
                     color=accent_for("watchlist")).pack(anchor="w", pady=(0, 8))

        selected_var = ctk.StringVar(value=self.selected_genre)

        sc = ctk.CTkScrollableFrame(wrapper, fg_color="transparent")
        sc.pack(fill="both", expand=True)

        ctk.CTkRadioButton(sc, text=f"{t('all')} ({total})",
                           value=t("all"), variable=selected_var,
                           fg_color=accent_for("watchlist")).pack(anchor="w", pady=4)

        for g, c in gens:
            ctk.CTkRadioButton(sc, text=f"{g} ({c})",
                               value=g, variable=selected_var,
                               fg_color=accent_for("watchlist")).pack(anchor="w", pady=4)

        actions = ctk.CTkFrame(wrapper, fg_color="transparent")
        actions.pack(fill="x", pady=(10, 0))
        ctk.CTkButton(actions, text=t("cancel"), fg_color="#EF4444",
                      command=win.destroy).pack(side="right", padx=(6, 0))
        ctk.CTkButton(actions, text=t("apply"), fg_color=accent_for("watchlist"),
                      command=lambda: self._apply_genre(win, selected_var.get())).pack(side="right")

    def _apply_genre(self, win, value):
        self.selected_genre = value or t("all")
        try:
            win.destroy()
        except Exception:
            pass
        self._render()

    def _genres_with_counts(self):
        items = storage.list_watchlist_movies(self.username)
        counts = {}
        for m in items:
            g = (m.get("genre") or "").strip()
            if not g:
                continue
            counts[g] = counts.get(g, 0) + 1
        return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
