import os
import streamlit as st

st.set_page_config(page_title="Netflix Power BI — Streamlit Host", page_icon="🎬", layout="wide")
st.title("🎬 Netflix Dashboard (Power BI embedded)")

# --- How to supply your Power BI embed URL ---
# Option A: put it in Streamlit Secrets as PBI_EMBED_URL
# Option B: hardcode below (pbi_url = "https://app.powerbi.com/view?r=...")
# Option C: type it into the textbox at runtime

pbi_url = st.secrets.get("PBI_EMBED_URL", "").strip()

with st.sidebar:
    st.header("Embed Settings")
    if not pbi_url:
        pbi_url = st.text_input(
            "Power BI 'Publish to web' URL",
            placeholder="https://app.powerbi.com/reportEmbed?reportId=25736d1c-5cbd-4462-9212-5b35b7ca7792&autoAuth=true&ctid=f372731b-ab11-4425-ae60-7130988374fd",
        ).strip()

    height = st.slider("IFrame height (px)", 600, 1400, 900, step=50)
    hide_nav = st.checkbox("Hide navigation pane", value=True)
    hide_filters = st.checkbox("Hide filter pane", value=True)

# Append pane params if requested (works with most Publish-to-web links)
params = []
if hide_nav:
    params.append("navContentPaneEnabled=false")
if hide_filters:
    params.append("filterPaneEnabled=false")

if pbi_url and params:
    sep = "&" if "?" in pbi_url else "?"
    pbi_url_render = f"{pbi_url}{sep}{'&'.join(params)}"
else:
    pbi_url_render = pbi_url

if not pbi_url_render:
    st.info("Paste your **Power BI Publish to web** embed URL in the sidebar to render the report.")
else:
    # Render the report via a simple iframe
    st.components.v1.html(
        f'''
        <div style="position:relative;padding-top:0;">
          <iframe
            title="Power BI"
            width="100%"
            height="{height}"
            src="{pbi_url_render}"
            frameborder="0"
            allowFullScreen="true">
          </iframe>
        </div>
        ''',
        height=height + 10,
        scrolling=True,
    )

st.caption(
    "Note: This uses **Publish to web** (public). For private/secure embeds you’ll need Azure AD + Embed Tokens "
    "and a backend service — ping me if you want that setup."
)
