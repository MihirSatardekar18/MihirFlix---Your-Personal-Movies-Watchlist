import customtkinter as ctk
from tkinter import messagebox
import json, os, re, threading, time
from theme import styled_label, TEXT_COLOR, ACCENT_PROFILE, CARD_COLOR
from datetime import datetime

DB_FILE = "data/contact_messages.json"

class ContactPage(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        
        styled_label(self, "📬 Contact Us", font=("Segoe UI", 28, "bold"),
                     color=ACCENT_PROFILE).pack(pady=(15, 5))
        styled_label(self, "Drop your queries below — we'll reply quickly.",
                     font=("Segoe UI", 14), color="#A7B0C0").pack(pady=(0, 20))

        self.add_entry("Your Name", "Enter full name")
        self.add_entry("Email Address", "Enter your email")
        
        styled_label(self, "Query Type", font=("Segoe UI", 14), color=TEXT_COLOR).pack(anchor="w", padx=12, pady=(8,0))
        self.query_type = ctk.CTkOptionMenu(self, values=["General", "Feedback", "Support", "Business"])
        self.query_type.pack(fill="x", padx=12, pady=(0,8))

        styled_label(self, "Message", font=("Segoe UI", 14), color=TEXT_COLOR).pack(anchor="w", padx=12)
        self.message_text = ctk.CTkTextbox(self, height=120)
        self.message_text.pack(fill="x", padx=12, pady=(0,4))

        self.submit_btn = ctk.CTkButton(self, text="Save Message", fg_color=ACCENT_PROFILE,
                                        hover_color="#ff4d6d", command=self._validate_and_save)
        self.submit_btn.pack(pady=12)

        # Ensure DB file exists
        self._init_db()

    def add_entry(self, label_text, placeholder):
        styled_label(self, label_text, font=("Segoe UI", 14), color=TEXT_COLOR).pack(anchor="w", padx=12, pady=(8,0))
        entry = ctk.CTkEntry(self, placeholder_text=placeholder)
        entry.pack(fill="x", padx=12, pady=(0,4))
        setattr(self, f"{label_text.lower().replace(' ', '_')}_entry", entry)

    def _init_db(self):
        os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
        if not os.path.exists(DB_FILE):
            with open(DB_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _validate_and_save(self):
        name = self.your_name_entry.get().strip()
        email = self.email_address_entry.get().strip()
        msg = self.message_text.get("1.0", "end").strip()

        if not all([name, email, msg]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Enter a valid email address.")
            return

        self.submit_btn.configure(text="Saving...", state="disabled")
        threading.Thread(target=self._save_message, args=(name, email, self.query_type.get(), msg)).start()

    def _save_message(self, name, email, query_type, message):
        try:
            # Load existing data
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Add new record
            data.append({
                "name": name,
                "email": email,
                "query_type": query_type,
                "message": message,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            # Save back
            with open(DB_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            messagebox.showinfo("Success", "Your message was saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save message: {e}")
        finally:
            self.submit_btn.configure(text="Save Message", state="normal")
            self.clear_form()

    def clear_form(self):
        self.your_name_entry.delete(0, "end")
        self.email_address_entry.delete(0, "end")
        self.query_type.set("General")
        self.message_text.delete("1.0", "end")
