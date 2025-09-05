# 🎬 Netflix Analytics Dashboard (Power BI → Streamlit)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/App-Streamlit-informational)
![Power BI](https://img.shields.io/badge/Report-Power%20BI-orange)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

A minimal Streamlit app that **embeds a Power BI report** using the public *Publish to web* URL—no extra UI, just the dashboard.

**Live demo:**  
[YOUR_STREAMLIT_APP_URL](https://netflix-analytics-dashboard-78z9dst6b4nsdjte6kvrmg.streamlit.app/)

---

## 🔎 Overview
- **Report authoring:** Power BI Desktop / Service  
- **Hosting:** Streamlit (serves a single full-screen `<iframe>` with the Power BI report)  
- **Goal:** Provide a clean, public link to view the Power BI dashboard without exposing the Service workspace.

---

## 🧱 How it works
The app renders your Power BI **Publish to web** URL inside an iframe and optionally hides filter & navigation panes:

```python
PBI_EMBED_URL = "https://app.powerbi.com/view?r=YOUR_EMBED_ID"
params = "filterPaneEnabled=false&navContentPaneEnabled=false"
sep = "&" if "?" in PBI_EMBED_URL else "?"
iframe_url = f"{PBI_EMBED_URL}{sep}{params}"

