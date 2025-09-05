# 🎬 Netflix Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/App-Streamlit-informational)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

An interactive **Streamlit** dashboard to explore Netflix titles by **type, year, genres, ratings, and countries**.  
Built for portfolio-grade analytics storytelling with clean filtering, KPIs, and Plotly charts.

---

## ✨ Features

- Sidebar filters: **Type**, **Release Year** range, **Top Genres**, **Top Countries**, **Keyword** search
- KPIs: **Total titles**, **Movies**, **TV Shows**, **Countries**
- Charts:
  - Top Genres (bar)
  - Titles by Release Year (area)
  - Titles by Rating (bar)
  - Top Countries (bar)
- Data table of filtered titles
- Works with your uploaded CSV or a small built-in sample (so the app always runs)

---

> If `data/netflix_titles.csv` is absent, you can upload a CSV from the app sidebar.

---

## 🧮 Data (expected columns)

The app is compatible with the common “Netflix titles” CSV schema (e.g., Kaggle).  
Useful columns (case-insensitive, extra columns are ignored):

- `type` — Movie / TV Show  
- `title` — Title name  
- `country` — Country (comma-separated)  
- `release_year` — Year of release (numeric)  
- `rating` — MPAA/TV rating (e.g., PG-13, TV-MA)  
- `listed_in` — Genres (comma-separated)  
- `date_added` — Date added to Netflix  
- `duration` — Minutes or Seasons  
- `description` — Short synopsis

> The app automatically **explodes** multi-valued `listed_in` and `country` into single values for filtering.

---

## 🚀 Quickstart (Local)

1) **Create and activate** a virtual env:
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
