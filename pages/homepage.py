# pages/homepage.py
import os, json
import customtkinter as ctk
from components.sidebar import Sidebar
from components.topbar import TopBar
from components.movie_card import MovieCard
from theme import styled_label, TEXT_COLOR, accent_for, BANNER_PATH, load_image, styled_button
from utils import storage
from utils.i18n import t, on_language_change, set_language

class HomePage(ctk.CTkFrame):
    def __init__(self, master, username, on_logout):
        super().__init__(master, fg_color="transparent")
        self.username = username
        self.on_logout = on_logout
        self.current_view = "home"

        # Apply saved language/theme BEFORE building UI
        self._apply_saved_prefs()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.sidebar = Sidebar(self, on_nav=self._handle_nav, username=username)
        self.sidebar.grid(row=0, column=0, sticky="nsw")

        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=0, column=1, sticky="nsew")

        self.selected_genre = t("all")

        on_language_change(self._on_lang_change)
        self.show_home()

    def _apply_saved_prefs(self):
        try:
            path = os.path.join("data", f"profile_{self.username}.json")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                lang = data.get("language")
                if lang:
                    set_language(lang)
                theme = data.get("theme")
                if theme in ("Light", "Dark"):
                    ctk.set_appearance_mode(theme)
        except Exception:
            pass

    def _on_lang_change(self, _code: str):
        try:
            self.sidebar.destroy()
        except Exception:
            pass
        self.sidebar = Sidebar(self, on_nav=self._handle_nav, username=self.username)
        self.sidebar.grid(row=0, column=0, sticky="nsw")

        # Reset "All" to translated label if filter is All
        if self.selected_genre.lower() in ("all", t("all").lower()):
            self.selected_genre = t("all")

        self._open_view(self.current_view)

    def _clear_content(self):
        for w in self.content.winfo_children():
            w.destroy()

    def _open_view(self, key: str):
        self.current_view = key
        pages = {
            "home": self.show_home,
            "watchlist": self.show_watchlist,
            "add_movie": self.show_add_movie,
            "profile": self.show_profile,
            "about": self.show_about,
            "contact": self.show_contact,
            "stats": self.show_stats
        }
        if key in pages:
            pages[key]()

    def _handle_nav(self, key):
        self._open_view(key)

    def show_home(self):
        self._clear_content()
        TopBar(self.content, f"🏠 {t('home')}", accent_for("home")).pack(fill="x", pady=(10, 10))

        banner_img = load_image(BANNER_PATH, size=(720, 180))
        if banner_img:
            ctk.CTkLabel(self.content, image=banner_img, text="").pack(padx=16, pady=(6, 10))

        row = ctk.CTkFrame(self.content, fg_color="transparent")
        row.pack(fill="x", padx=16, pady=(0, 8))
        styled_label(row, t("tagline"), color=TEXT_COLOR, font=("Segoe UI", 18, "bold")).pack(side="left")

        filter_row = ctk.CTkFrame(self.content, fg_color="transparent")
        filter_row.pack(fill="x", padx=16, pady=(0, 10))
        if self.selected_genre != t("all"):
            styled_label(filter_row, f"{t('filter_by_genre')}: {self.selected_genre}",
                         color="white", font=("Segoe UI", 14, "bold")).pack(side="left", padx=(0, 10))
            styled_button(filter_row, t("clear"), self._clear_genre, color="#6B7280").pack(side="left", padx=(0, 10))
        styled_button(filter_row, t("select_genre"), self._open_genre_picker, color=accent_for("home")).pack(side="right")

        self._render_home_list()

    def _render_home_list(self):
        for w in list(self.content.winfo_children()):
            if isinstance(w, ctk.CTkScrollableFrame):
                w.destroy()

        sc = ctk.CTkScrollableFrame(self.content, fg_color="transparent")
        sc.pack(fill="both", expand=True, padx=16, pady=10)

        movies = storage.get_catalog()[::-1]
        if self.selected_genre != t("all"):
            sel = (self.selected_genre or "").strip().lower()
            movies = [m for m in movies if (m.get("genre") or "").strip().lower() == sel]

        if not movies:
            styled_label(sc, t("no_movies_genre"), color="#A7B0C0").pack(pady=20)
            return

        for m in movies:
            MovieCard(sc, movie=m, username=self.username, refresh_callback=self.show_home).pack(fill="x", pady=6, padx=4)

    def _clear_genre(self):
        self.selected_genre = t("all")
        self.show_home()

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

        TopBar(wrapper, t("filter_by_genre"), accent_for("home")).pack(fill="x", pady=(0, 8))

        selected_var = ctk.StringVar(value=self.selected_genre)

        sc = ctk.CTkScrollableFrame(wrapper, fg_color="transparent")
        sc.pack(fill="both", expand=True)

        ctk.CTkRadioButton(sc, text=f"{t('all')} ({total})",
                           value=t("all"), variable=selected_var,
                           fg_color=accent_for("home")).pack(anchor="w", pady=4)

        for g, c in gens:
            ctk.CTkRadioButton(sc, text=f"{g} ({c})",
                               value=g, variable=selected_var,
                               fg_color=accent_for("home")).pack(anchor="w", pady=4)

        actions = ctk.CTkFrame(wrapper, fg_color="transparent")
        actions.pack(fill="x", pady=(10, 0))
        ctk.CTkButton(actions, text=t("cancel"), fg_color="#EF4444",
                      command=win.destroy).pack(side="right", padx=(6, 0))
        ctk.CTkButton(actions, text=t("apply"), fg_color=accent_for("home"),
                      command=lambda: self._apply_genre(win, selected_var.get())).pack(side="right")

    def _apply_genre(self, win, value):
        self.selected_genre = value or t("all")
        try:
            win.destroy()
        except Exception:
            pass
        self.show_home()

    def _genres_with_counts(self):
        items = storage.get_catalog()
        counts = {}
        for m in items:
            g = (m.get("genre") or "").strip()
            if not g: continue
            counts[g] = counts.get(g, 0) + 1
        return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))

    # other pages
    def show_watchlist(self):
        from pages.watchlist_page import WatchlistPage
        self._clear_content()
        WatchlistPage(self.content, self.username).pack(fill="both", expand=True)

    def show_add_movie(self):
        self._clear_content()
        from pages.add_movie_page import AddMoviePage
        AddMoviePage(self.content, username=self.username, on_done=self.show_home).pack(fill="both", expand=True)

    def show_profile(self):
        self._clear_content()
        from pages.profile_page import ProfilePage
        ProfilePage(self.content, username=self.username,
                    on_logout=self.on_logout, on_show_stats=self.show_stats).pack(fill="both", expand=True)

    def show_about(self):
        self._clear_content()
        from pages.about_page import AboutPage
        AboutPage(self.content).pack(fill="both", expand=True)

    def show_contact(self):
        self._clear_content()
        from pages.contact_page import ContactPage
        ContactPage(self.content).pack(fill="both", expand=True)

    def show_stats(self):
        self._clear_content()
        from pages.stats_page import StatsPage
        StatsPage(self.content, username=self.username).pack(fill="both", expand=True)
