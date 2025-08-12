import io, csv
import pandas as pd
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="CalAIM TXT Converter")
st.title("CalAIM TXT Converter (.xlsx → .TXT)")

uploaded = st.file_uploader("Upload .xlsx", type=["xlsx"])

def process_excel(file):
    df = pd.read_excel(file)
    df.columns = df.columns.str.lower()
    if "address2" in df.columns:
        df["address2"] = df["address2"].where(pd.notnull(df["address2"]), None)
    if "patientvmcmcmrn" in df.columns:  # typo-proof? use your exact column name
        pass
    if "patientvmcmrn" in df.columns:
        df["patientvmcmrn"] = df["patientvmcmrn"].fillna("").apply(
            lambda x: str(int(x)) if str(x).strip() != "" else ""
        )
    buf = io.StringIO()
    df.to_csv(buf, sep="|", index=False, quoting=csv.QUOTE_NONE, encoding="utf-8")
    return buf.getvalue()

if uploaded:
    try:
        txt_data = process_excel(uploaded)
        fname = f"CalAim_SoberingCenter_{datetime.now().strftime('%Y%m%d')}.TXT"
        st.download_button("Download TXT", txt_data.encode("utf-8"), file_name=fname, mime="text/plain")
        st.success("Converted. Download above.")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Upload a .xlsx file to begin.")
