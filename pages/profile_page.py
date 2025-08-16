# pages/profile_page.py
import os, json
import customtkinter as ctk
from theme import styled_label, styled_button, TEXT_COLOR, ACCENT_PROFILE, CARD_COLOR, accent_for
from utils.i18n import t, set_language
from utils import storage
from tkinter import filedialog, messagebox
from PIL import Image

LANG_CODES = ["en", "hi", "mr", "fr", "es", "de", "it", "bn", "ta", "te"]

class ProfilePage(ctk.CTkScrollableFrame):
    def __init__(self, master, username, on_logout=None, on_show_stats=None):
        super().__init__(master, fg_color="transparent")
        self.username = username
        self.on_logout = on_logout
        self.on_show_stats = on_show_stats
        self.data_file = os.path.join("data", f"profile_{username}.json")
        self.profile_img = None
        self._load_data()

        styled_label(self, t("profile_settings"), font=("Segoe UI", 24, "bold"),
                     color=ACCENT_PROFILE).pack(pady=(20, 10))

        # Profile picture
        self.pic_label = ctk.CTkLabel(self, text="[Profile Picture]",
                                      width=120, height=120,
                                      fg_color=CARD_COLOR, text_color=TEXT_COLOR,
                                      corner_radius=60)
        self.pic_label.pack(pady=10)
        styled_button(self, t("upload_change_picture"), self._upload_pic,
                      color=ACCENT_PROFILE).pack()
        if self.data.get("profile_pic") and os.path.exists(self.data["profile_pic"]):
            self._set_pic(self.data["profile_pic"])

        # Info fields
        self.full_name = self._entry(t("full_name"), self.data.get("full_name", ""))
        self.username_entry = self._entry(t("username"), self.data.get("username", self.username))
        self.email = self._entry(t("email"), self.data.get("email", ""))
        self.phone = self._entry(t("phone"), self.data.get("phone", ""))
        self.dob = self._entry(t("dob"), self.data.get("dob", ""))
        self.gender = self._entry(t("gender"), self.data.get("gender", ""))

        # Language (codes) — change applies instantly
        styled_label(self, t("language_preference"), color=TEXT_COLOR).pack(pady=(10, 2))
        self.lang_pref = ctk.CTkOptionMenu(self, values=LANG_CODES,
                                           command=self._on_language_selected)
        self.lang_pref.set(self.data.get("language", "en"))
        self.lang_pref.pack()

        # Theme (instant apply)
        styled_label(self, t("theme"), color=TEXT_COLOR).pack(pady=(10, 2))
        self.theme_mode = ctk.CTkOptionMenu(self, values=["Light", "Dark"],
                                            command=lambda mode: ctk.set_appearance_mode(mode))
        self.theme_mode.set(self.data.get("theme", "Dark"))
        self.theme_mode.pack()

        styled_label(self, t("privacy"), color=TEXT_COLOR).pack(pady=(10, 2))
        self.privacy = ctk.CTkOptionMenu(self, values=[t("public"), t("private")])
        self.privacy.set(self.data.get("privacy", t("private")))
        self.privacy.pack()

        styled_label(self, t("notifications"), color=TEXT_COLOR).pack(pady=(10, 2))
        self.notifications = ctk.CTkOptionMenu(self, values=["All", "Important Only", "None"])
        self.notifications.set(self.data.get("notifications", "All"))
        self.notifications.pack()

        # Save / Update
        styled_button(self, t("save_update_profile"), self._save_profile,
                      color=ACCENT_PROFILE).pack(pady=12)

        # Extras
        styled_button(self, t("change_password"),
                      lambda: messagebox.showinfo(t("change_password"), "Password change flow"),
                      color="#f59e0b").pack(pady=4)

        styled_label(self, t("linked_accounts"), color=TEXT_COLOR).pack(pady=(12, 4))
        for svc in ["Google", "Facebook"]:
            styled_button(self, f"{t('linked_accounts')}: {svc}",
                          lambda s=svc: messagebox.showinfo("Link", f"{s} linking UI"),
                          color="#3b82f6").pack(pady=2)

        styled_label(self, t("recently_watched"), color=TEXT_COLOR).pack(pady=(12, 4))
        for m in (storage.get_recent_watched(self.username) or []):
            styled_label(self, f"• {m.get('title')}", color="#A7B0C0").pack(anchor="w", padx=20)

        if callable(self.on_show_stats):
            styled_button(self, t("view_my_stats"),
                          self.on_show_stats, color=accent_for("stats")).pack(pady=(12, 4))

        styled_button(self, t("delete_account"),
                      lambda: messagebox.showwarning(t("delete_account"), "Account deletion flow"),
                      color="#dc2626").pack(pady=(12, 4))

        if callable(self.on_logout):
            styled_button(self, t("logout"), self._confirm_logout,
                          color="#ef4444").pack(pady=(20, 20))

    def _entry(self, placeholder, value=""):
        e = ctk.CTkEntry(self, placeholder_text=placeholder,
                         fg_color=CARD_COLOR, text_color=TEXT_COLOR,
                         placeholder_text_color="#A7B0C0")
        if value:
            e.insert(0, value)
        e.pack(fill="x", padx=20, pady=4)
        return e

    def _set_pic(self, path):
        try:
            img = Image.open(path).resize((120, 120))
            self.profile_img = ctk.CTkImage(img, size=(120, 120))
            self.pic_label.configure(image=self.profile_img, text="")
        except Exception:
            pass

    def _upload_pic(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.webp")])
        if path:
            self._set_pic(path)
            self.data["profile_pic"] = path

    def _on_language_selected(self, code: str):
        # Instant apply on select; HomePage listener will rebuild current view
        set_language(code)

    def _load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def _save_profile(self):
        self.data.update({
            "full_name": self.full_name.get(),
            "username": self.username_entry.get(),
            "email": self.email.get(),
            "phone": self.phone.get(),
            "dob": self.dob.get(),
            "gender": self.gender.get(),
            "language": self.lang_pref.get(),
            "theme": self.theme_mode.get(),
            "privacy": self.privacy.get(),
            "notifications": self.notifications.get(),
            "profile_pic": self.data.get("profile_pic", "")
        })

        # Ensure chosen language & theme are applied (in case user only saved)
        set_language(self.lang_pref.get())
        ctk.set_appearance_mode(self.theme_mode.get())

        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

        messagebox.showinfo(t("profile_settings"), t("profile_saved"))

    def _confirm_logout(self):
        if messagebox.askyesno(t("logout"), t("logout") + "?"):
            if callable(self.on_logout):
                self.on_logout()
