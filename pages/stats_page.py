import customtkinter as ctk
from theme import styled_label, TITLE_FONT, accent_for
from utils import storage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from datetime import datetime

class StatsPage(ctk.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master, fg_color="transparent")
        accent = accent_for("stats")
        styled_label(self, "📊 Movie Analytics Dashboard", font=TITLE_FONT, color=accent).pack(pady=(16, 10))

        catalog = storage.get_catalog()
        watched = [m for m in catalog if storage.is_watched(username, m.get("id"))]
        wl = storage.list_watchlist_movies(username)

        # --- Summary ---
        total = len(catalog)
        watched_count = len(watched)
        wl_count = len(wl)
        watched_pct = (watched_count / total * 100) if total else 0

        styled_label(self, f"🎬 Total movies: {total}").pack()
        styled_label(self, f"✅ Watched: {watched_count} ({watched_pct:.1f}%)").pack()
        styled_label(self, f"📝 In Watchlist: {wl_count}").pack(pady=(0, 12))

        if not catalog:
            styled_label(self, "No data available", color="#A7B0C0").pack(pady=10)
            return

        # --- Chart Data ---
        genre_counts = {}
        for m in catalog:
            g = (m.get("genre") or "Unknown").strip()
            genre_counts[g] = genre_counts.get(g, 0) + 1

        colors = [
            (random.random()*0.6+0.4, random.random()*0.6+0.4, random.random()*0.6+0.4)
            for _ in genre_counts
        ]

        # Timeline (Watched history)
        timeline = []
        for m in watched:
            date_str = m.get("watched_date") or m.get("date_added")
            try:
                dt = datetime.strptime(date_str, "%Y-%m-%d")
                timeline.append((dt, m.get("title", "Unknown"), m.get("rating") or 0))
            except:
                pass
        timeline.sort(key=lambda x: x[0])

        # --- Matplotlib Figure ---
        fig = Figure(figsize=(9, 6), dpi=100)

        # 1️⃣ Genre Bar Chart
        ax1 = fig.add_subplot(221)
        genres = list(genre_counts.keys())
        counts = list(genre_counts.values())
        bars = ax1.bar(genres, counts, color=colors, edgecolor="black", linewidth=0.7)
        ax1.set_title("Movies by Genre", fontsize=10, fontweight="bold")
        ax1.tick_params(axis="x", rotation=30)
        ax1.grid(axis="y", linestyle="--", alpha=0.6)
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2, height + 0.1, str(height),
                     ha='center', va='bottom', fontsize=8)

        # 2️⃣ Genre Pie Chart
        ax2 = fig.add_subplot(222)
        ax2.pie(counts, labels=genres, autopct='%1.1f%%',
                colors=colors, textprops={'fontsize': 8})
        ax2.set_title("Genre Distribution", fontsize=10, fontweight="bold")

        # 3️⃣ Watched vs Unwatched
        ax3 = fig.add_subplot(223)
        uw = total - watched_count
        ax3.pie([watched_count, uw], labels=["Watched", "Unwatched"],
                autopct='%1.1f%%', colors=[(0.4,0.8,0.4),(0.9,0.5,0.5)],
                startangle=90, textprops={'fontsize': 8})
        ax3.set_title("Overall Progress", fontsize=10, fontweight="bold")

        # 4️⃣ Timeline Chart
        ax4 = fig.add_subplot(224)
        if timeline:
            dates = [t[0] for t in timeline]
            ratings = [t[2] for t in timeline]
            titles = [t[1] for t in timeline]
            ax4.plot(dates, ratings, marker='o', color=accent, linewidth=1.5)
            for d, r, title in zip(dates, ratings, titles):
                ax4.text(d, r+0.1, title, fontsize=6, rotation=30, ha='left')
            ax4.set_ylim(0, 10)
            ax4.set_title("Watched History (Ratings over Time)", fontsize=10, fontweight="bold")
            ax4.set_ylabel("Rating")
            ax4.grid(True, linestyle="--", alpha=0.6)
        else:
            ax4.text(0.5, 0.5, "No watch history", ha='center', va='center', fontsize=9)

        # --- Render in Tkinter ---
        fig.tight_layout(pad=3.0)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)
