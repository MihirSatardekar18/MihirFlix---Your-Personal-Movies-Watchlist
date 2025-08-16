# 🎬 **MihirFlix – Premium OTT‑Style Movie Watchlist App**  

![MihirFlix Banner](assets/readme/banner.png)

> 🚀 _Your personal, multilingual, cinematic movie hub with watchlist, trailers, stats & more._

---

## ✨ Features

### 🎯 **Core Functionality**
- 📜 **Movie Catalog** – Browse movies across multiple languages & genres.
- ⭐ **Watchlist** – Add/remove movies from your personal watchlist.
- ✅ **Watched Toggle** – One-click to mark as watched/unwatched with persistent history.
- 🎥 **Watch Trailer** – Direct YouTube trailer integration for instant preview.
- 📊 **Advanced Statistics** – Multi-chart Matplotlib dashboard:
  - Genre bar chart & pie chart
  - Watched vs Unwatched overview
  - Ratings timeline with movie annotations
- 📩 **Contact Page** – Professional form with validation, live character counter, JSON storage.
- 👤 **Profile Page** – Persistent profile/settings with instant theme & language switching.

---

## 🖼️ **Screenshots**

| Home Page | Watchlist Page | Stats Dashboard |
|-----------|----------------|-----------------|
| ![](assets/readme/home.png) | ![](assets/readme/watchlist.png) | ![](assets/readme/stats.png) |

---

## 🛠 **Tech Stack**
- **Python 3.10+**
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) – Modern Tkinter UI
- **Matplotlib** – Advanced Data Visualization
- **JSON Storage** – Persistent local database
- **Webbrowser API** – Direct trailer playback

---

## 📂 **Project Structure**
```plaintext
MihirFlix Movies Watchlist/
│
├── assets/
│   ├── posters/          # Movie poster images
│   └── readme/           # Banner & screenshots
│
├── components/           # UI components (Sidebar, MovieCard, etc.)
├── pages/                # Individual app pages (Home, Watchlist, Stats, etc.)
├── utils/                # Storage, helpers, i18n, etc.
├── data/                 # JSON database (movies, users, contact messages)
├── main.py                # Entry point
└── README.md
