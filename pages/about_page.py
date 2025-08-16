import customtkinter as ctk
from theme import styled_label, TEXT_COLOR, ACCENT_PROFILE

class AboutPage(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        # Heading
        styled_label(self, "About Us (MihirFlix)", font=("Segoe UI", 26, "bold"),
                     color=ACCENT_PROFILE).pack(pady=(20, 10))
        styled_label(self, "3rd Year Diploma Python Internship Project",
                     font=("Segoe UI", 16, "italic"), color="#A7B0C0").pack(pady=(0, 10))

        # Tagline
        ctk.CTkLabel(
            self,
            text="@ V2V EdTech LLP\nWelcome to MihirFlix – Your Personal Movies Watchlist & Streaming Companion",
            font=("Segoe UI", 18, "bold"),
            text_color=TEXT_COLOR,
            wraplength=800,
            justify="center"
        ).pack(pady=(10, 4))

        ctk.CTkLabel(
            self,
            text="All your favourite movies, in one place – Anytime, Anywhere.",
            font=("Segoe UI", 14, "italic"),
            text_color="#FACC15",
            wraplength=800,
            justify="center"
        ).pack(pady=(0, 20))

        # Introduction
        styled_label(self, "Introduction", font=("Segoe UI", 20, "bold"),
                     color=ACCENT_PROFILE).pack(anchor="w", padx=16, pady=(10, 4))
        ctk.CTkLabel(
            self,
            text="MihirFlix is a modern movie watchlist application designed to keep all your favourite films organized, easy to access, and beautifully displayed. Whether you want to track, watch, or discover new movies – MihirFlix has you covered.",
            font=("Segoe UI", 14),
            text_color=TEXT_COLOR,
            wraplength=800,
            justify="left"
        ).pack(anchor="w", padx=16, pady=(0, 10))

        # Mission
        styled_label(self, "Our Mission", font=("Segoe UI", 20, "bold"),
                     color=ACCENT_PROFILE).pack(anchor="w", padx=16, pady=(10, 4))
        ctk.CTkLabel(
            self,
            text="Our mission is to provide an elegant, user-friendly, and customizable platform for movie lovers. With modern features like poster previews, ratings, recommendations, and video playback, MihirFlix aims to make your movie experience seamless and enjoyable.",
            font=("Segoe UI", 14),
            text_color=TEXT_COLOR,
            wraplength=800,
            justify="left"
        ).pack(anchor="w", padx=16, pady=(0, 10))

        # Features
        styled_label(self, "Key Features", font=("Segoe UI", 20, "bold"),
                     color=ACCENT_PROFILE).pack(anchor="w", padx=16, pady=(10, 4))
        features = [
            "Movie Watchlist with Posters & Ratings",
            "Add Movies with Genre, Language & Video",
            "Personalised Recommendations",
            "Multi-language Support",
            "Light & Dark Mode for Comfort Viewing"
        ]
        for feat in features:
            ctk.CTkLabel(
                self,
                text=f"• {feat}",
                font=("Segoe UI", 14),
                text_color=TEXT_COLOR,
                wraplength=800,
                justify="left"
            ).pack(anchor="w", padx=32)

        # Vision
        styled_label(self, "Vision", font=("Segoe UI", 20, "bold"),
                     color=ACCENT_PROFILE).pack(anchor="w", padx=16, pady=(10, 4))
        ctk.CTkLabel(
            self,
            text="We envision MihirFlix as not just an app, but a personal movie companion – where you can keep your entertainment world beautifully organized and always accessible.",
            font=("Segoe UI", 14),
            text_color=TEXT_COLOR,
            wraplength=800,
            justify="left"
        ).pack(anchor="w", padx=16, pady=(0, 10))

        # Credits
        styled_label(self, "Credits / Developer Note", font=("Segoe UI", 20, "bold"),
                     color=ACCENT_PROFILE).pack(anchor="w", padx=16, pady=(10, 4))
        ctk.CTkLabel(
            self,
            text='"MihirFlix is developed by Mihir Satardekar as a personal project inspired by modern OTT platforms like Netflix and JioCinema."',
            font=("Segoe UI", 14, "italic"),
            text_color=TEXT_COLOR,
            wraplength=800,
            justify="left"
        ).pack(anchor="w", padx=16, pady=(0, 10))

        # Footer
        ctk.CTkLabel(
            self,
            text="# One Man Army\n© 2025 MihirFlix Movies Watchlist. All Rights Reserved.",
            font=("Segoe UI", 12),
            text_color="#A7B0C0",
            wraplength=800,
            justify="center"
        ).pack(pady=(20, 10))
