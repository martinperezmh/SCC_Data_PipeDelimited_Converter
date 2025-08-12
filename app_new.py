{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38c4bfc2-3e23-44e6-aa01-ff0bca1d6f04",
   "metadata": {},
   "outputs": [],
   "source": [
    "import io, csv\n",
    "import pandas as pd\n",
    "from datetime import datetime\n",
    "import streamlit as st\n",
    "\n",
    "st.set_page_config(page_title=\"CalAIM TXT Converter\", layout=\"centered\")\n",
    "st.title(\"CalAIM TXT Converter (.xlsx ➜ .TXT)\")\n",
    "\n",
    "uploaded = st.file_uploader(\"Drag & drop your .xlsx here\", type=[\"xlsx\"])\n",
    "\n",
    "# Optional: let the user pick a sheet after upload\n",
    "sheet_name = st.text_input(\"Sheet name (leave blank for first sheet)\", \"\")\n",
    "\n",
    "def process_excel(file, sheet):\n",
    "    # Read Excel\n",
    "    df = pd.read_excel(file, sheet_name=sheet if sheet else 0)\n",
    "\n",
    "    # Case-insensitive columns\n",
    "    df.columns = df.columns.str.lower()\n",
    "\n",
    "    # address2 -> None\n",
    "    if \"address2\" in df.columns:\n",
    "        df[\"address2\"] = df[\"address2\"].where(pd.notnull(df[\"address2\"]), None)\n",
    "\n",
    "    # patientvmcmrn -> strip trailing zeros by coercing to int-string (empty stays empty)\n",
    "    if \"patientvmcmrn\" in df.columns:\n",
    "        df[\"patientvmcmrn\"] = df[\"patientvmcmrn\"].fillna(\"\").apply(\n",
    "            lambda x: str(int(x)) if str(x).strip() != \"\" else \"\"\n",
    "        )\n",
    "\n",
    "    # Build pipe-delimited TXT in-memory with no quoting\n",
    "    buf = io.StringIO()\n",
    "    df.to_csv(buf, sep=\"|\", index=False, quoting=csv.QUOTE_NONE, encoding=\"utf-8\")\n",
    "    return buf.getvalue()\n",
    "\n",
    "if uploaded:\n",
    "    try:\n",
    "        txt_data = process_excel(uploaded, sheet_name.strip())\n",
    "        current_date = datetime.now().strftime(\"%Y%m%d\")\n",
    "        filename = f\"CalAim_SoberingCenter_{current_date}.TXT\"\n",
    "\n",
    "        st.success(\"File processed! Click below to download.\")\n",
    "        st.download_button(\n",
    "            label=\"Download TXT\",\n",
    "            data=txt_data.encode(\"utf-8\"),\n",
    "            file_name=filename,\n",
    "            mime=\"text/plain\",\n",
    "        )\n",
    "\n",
    "        # Show a small preview\n",
    "        st.subheader(\"Preview\")\n",
    "        st.text(txt_data.splitlines()[0] if txt_data else \"\")\n",
    "    except Exception as e:\n",
    "        st.error(f\"Error: {e}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
