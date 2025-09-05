# app.py — minimal Streamlit host for a Power BI report (no UI, just the iframe)

import streamlit as st

st.set_page_config(layout="wide", page_title="Dashboard")
PBI_EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=25736d1c-5cbd-4462-9212-5b35b7ca7792&autoAuth=true&ctid=f372731b-ab11-4425-ae60-7130988374fd" 

st.components.v1.html(
    f"""
    <iframe
        title="Power BI Report"
        width="100%"
        height="100%"
        src="{PBI_EMBED_URL}"
        frameborder="0"
        allowfullscreen="true"
        style="position:fixed;top:0;left:0;bottom:0;right:0;width:100%;height:100vh;border:none;margin:0;padding:0;overflow:hidden;z-index:999999;">
    </iframe>
    """,
    height=900,  # container height (iframe uses full viewport height)
)
