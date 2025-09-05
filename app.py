import streamlit as st

st.set_page_config(layout="wide", page_title="Netflix Dashboard", page_icon="🎬")

# 👉 put your Publish-to-web URL here
PBI_EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=25736d1c-5cbd-4462-9212-5b35b7ca7792&autoAuth=true&ctid=f372731b-ab11-4425-ae60-7130988374fd"

# Hide filter & nav panes (works on Publish-to-web links)
params = "filterPaneEnabled=false&navContentPaneEnabled=false"
sep = "&" if "?" in PBI_EMBED_URL else "?"
iframe_url = f"{PBI_EMBED_URL}{sep}{params}"

st.components.v1.html(
    f"""
    <style>
      html, body, [data-testid="stAppViewContainer"] {{ height: 100%; margin: 0; padding: 0; }}
      .fullframe {{ position: fixed; inset: 0; border: 0; width: 100%; height: 100vh; }}
    </style>
    <iframe class="fullframe"
            title="Power BI Report"
            src="{iframe_url}"
            allowfullscreen="true"></iframe>
    """,
    height=1000,  # container height; iframe itself uses 100vh
)
